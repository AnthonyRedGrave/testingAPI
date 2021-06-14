from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from django.contrib.auth.models import User
from test_api.models import Question, Answer
from .models import Result, UserAnswer, IntermediateResult


class IntermediateResultChoicesField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        # показывать только те промежуточные результаты, которые относятся к пользователю и еще не имеющие ответов на вопросы
        queryset = IntermediateResult.objects.filter(user = user, is_done = False)
        return queryset


class QuestionChoicesField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        queryset = []
        for int_result in IntermediateResult.objects.filter(user = user, is_done = False):
            for question in int_result.quiz.questions.all():
                queryset.append(question)
        return queryset


class UserAnswerSerializer(serializers.ModelSerializer):
    intermediate_result = IntermediateResultChoicesField()

    class Meta:
        model = UserAnswer
        fields = ['id', 'text', 'intermediate_result', 'question', 'user']
        read_only_fields = ('user', )

    def validate(self, data):
        user = self.context['request'].user
        # если пользователь еще не отвечал на этот вопрос
        print(data)
        if UserAnswer.objects.filter(question=data['question'], user=user):
            raise serializers.ValidationError({"question": 'Вы уже отвечали на этот вопрос!'})
        return data

    def create(self, validated_data):

        user = self.context['request'].user
        user_answer = UserAnswer.objects.create(text=validated_data['text'],
                                                intermediate_result=validated_data['intermediate_result'],
                                                question=validated_data['question'],
                                                user=user
                                                )
        quiz_num_questions = validated_data['intermediate_result'].quiz.number_questions
        quiz_questions = validated_data['intermediate_result'].quiz.questions.all()
        num_user_answers = len(validated_data['intermediate_result'].answers.all())
        user_answers = validated_data['intermediate_result'].answers.all()
        if num_user_answers == quiz_num_questions:  # если на все вопросы дан ответ
            result = []
            score = 0
            correct_answer = None
            multiplier = 100 / quiz_num_questions
            for i in range(quiz_num_questions):
                print(quiz_questions[i])
                question_answers = Answer.objects.filter(question=quiz_questions[i])
                for ans in question_answers:
                    if ans.text == user_answers[i].text:
                        if ans.correct:  # если на вопрос дан правильный ответ
                            score += 1
                            correct_answer = ans.text
                            result.append(
                                {quiz_questions[i].text: {'correct': correct_answer, 'answered': user_answers[i].text}})
                    else:
                        if ans.correct:
                            correct_answer = ans.text
                            result.append({quiz_questions[i].text: {'correct': correct_answer,
                                                                    'wrong_answered': user_answers[i].text}})

            score_ = score * multiplier
            result_data = {'score': score_, 'result': result}

            int_res = IntermediateResult.objects.get(id = validated_data['intermediate_result'].id)
            int_res.is_done = True
            int_res.save()
            Result.objects.create(quiz=validated_data['intermediate_result'].quiz,
                                  user=user,
                                  score=score_,
                                  result_data=result_data)
            raise serializers.ValidationError("Ваш результат записан!")
        return user_answer



class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ['id', 'quiz', 'score', 'result_data']


class IntermediateResultSerializer(serializers.ModelSerializer):
    answers = UserAnswerSerializer(many=True)

    class Meta:
        model = IntermediateResult
        fields = ['id', 'quiz', 'user', 'answers', 'is_done']
        read_only_fields = ('user', )







