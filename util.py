#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import random
import verb

reflections = {
    "я": "вы",
    "ты": "я",
    "тебя": "вас",
    "тебе": "вам",
    "тобой": "вами",
    "о тебе": "о вас",
    "твой": "ваш",
    "мой": "ваш",
    "меня": "вас",
    "мной": "вами",
    "они": "их",
}


class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Пары это список шаблонов и ответов.
        шаблон - это регулярное выражение, соответствующее сообщению пользователя,
        например Мне нравится (. *). Для каждого такого шаблона список возможных ответов
        дается, например, [«Почему тебе нравится% 1», «Тебе когда-нибудь не нравился% 1»]. текст
        который соответствует разделенным в скобках разделам шаблонов (например, *), сопоставляется с
        пронумерованные позиции в ответах, например, % 1.

        """

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        """
        Заменяем местоимения        e.g. "I'm" -> "you are"
        """
        str = verb.verbchange(str)
        #print(str)
        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response



    def respond(self, str):

        # проверяем по каждому патерну
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            if match:
                resp = random.choice(response)  
                resp = self._wildcards(resp, match)  

                # обработка пунктуации
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"

                return resp



