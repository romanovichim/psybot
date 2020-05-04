#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from util import Chat, reflections


pairs = (
    (
        r"Мне нужно (.*)", 
        (
            "Почему вам нужно %1?",
            "Вам правда станет лучше если вы получите %1?",
            "Вам точно нужно %1?",
        ),
    ),
    (
        r"Я хочу (.*)", 
        (
            "Почему вы хотите %1?",
            "Вам правда станет лучше если вы получите %1?",
            "Вы точно хотите %1?",
        ),
    ),
    (
        r"Почему ты не (.*)",
        (
            "Вы правда думаешь что я не %1?",
            "Возможно, рано или поздно, я буду %1.",
            "Вы правда хотите чтобы я %1?",
        ),
    ),
    (
        r"Почему вы не (.*)",
        (
            "Вы правда думаешь что я не %1?",
            "Возможно, рано или поздно, я буду %1.",
            "Вы правда хотите чтобы я %1?",
        ),
    ),
    (
        r"Почему я не могу (.*)",
        (
            "Вы думаете вы должны быть способны %1?",
            "Если бы вы могли %1, что бы вы сделали?",
            "Я не знаю, почему вы не можете %1?",
            "Вы правда пытались ?",
        ),
    ),
    (
        r"Я не могу (.*)",
        (
            "Почему вы решили что не можете %1?",
            "Может вы могли бы %1 если бы попытались.",
            "Что требуется чтобы вы смогли %1?",
        ),
    ),
    (
        r"Я (.*)",
        (
            "Вы решили поговорить со мной потому что вы %1?",
	    "Как то что вы %1 заставляет вас себя чувствовать?",
            "Почему вы решили рассказать что вы %1?",
            "Почему, по вашему, вы %1?",
        ),
    ),
    (
        r"Ты (.*)",
        (
            "Почему вам важно, являюсь ли я %1?",
            "Вы хотели чтобы я не был %1?",
            "Возможно, вы верите что я %1.",
            "Возможно, я %1 -- что вы думаете по этому поводу?",
        ),
    ),
    (
        r"Что (.*)",
        (
            "Почему вы спрашиваете?",
            "Как вам поможет ответ на это?",
            "Как вы думаете?",
        ),
    ),
    (
        r"Как (.*)",
        (
            "А как по-вашему?",
            "Может вы сами можете ответить на свой вопрос.",
            "Что вы на самом деле хотите спросить?",
        ),
    ),
    (
        r"Потому что(.*)",
        (
            "Это точно настоящая причина?",
            "Какие еще ответы приходят вам на ум?",
            "Как мы можем это применить ко всему остальному?",
            "Если %1, что еще может быть правдой?",
        ),
    ),
    (
        r"(.*) извини (.*)",
        (
            "Есть много случаев когда нам на самом деле не нужно извиняться.",
            "Что вы чувствуете когда вы извиняетесь?",
        ),
    ),
    (
        r"Привет(.*)",
        (
            "Привет... Я рад что ты смогла сегодня зайти сюда.",
            "Привет.. Как вы сегодня?",
            "Привет, как вы себя чувствуете сегодня?",
        ),
    ),
    (
        r"Я думаю (.*)",
        ("У вас нет никаких сомнений в том что  %1?", "Вы действительно так думаешь?", "... Но вы не уверены %1?"),
    ),
    (
        r"(.*) друг (.*)", 
        (
            "Расскажи мне еще о своих друзьях.",
            "Что вам приходит на ум когда вы говорите о друге?",
            "Почему бы вам не рассказать мне о своем друге детства?",
        ),
    ),
    (
        r"(.*) подруга (.*)", 
        (
            "Расскажи мне еще о своих детских подругах.",
            "Что вам приходит на ум когда вы говоритк о подруге?",
            "Почему бы вам не рассказать мне о своей подруге детства?",
        ),
    ),
    (r"Да", ("Вы звучите достаточно уверенно в этом.", "Окей, давайте вы расскажешь об этом поподробнее?")),
    (
        r"(.*) компьютер(.*)", 
        (
            "Вы говорите про меня?",
            "Вы чувствуете себя странно от того что говорите с компьютером?",
            "Что вы чувствуете по поводу компьютеров?",
            "Вас напрягают компьютеры?",
        ),
    ),
    (
        r"(.*) бот(.*)", 
        (
            "Вы говорите про меня?",
            "Вы чувствуете себя странно от того что вы говорите с компьютером?",
            "Что вы чувствуете по поводу компьютеров?",
            "Вас напрягают компьютеры?",
        ),
    ),
    (
        r"Может это (.*)", 
        (
            "Вы думаешь это %1?",
            "Может это действительно %1 -- что вы про это думаете?",
            "Если бы это было %1, что бы вы делали?",
            "Вполне возможно что это %1.", 
        ),
    ),
    (
        r"Это (.*)", 
        (
            "Звучите очень уверенно в этом.",
            "А если бы я сказал вам что это скорее всего не %1, что бы вы чувствовали?",
        ),
    ),
    (
        r"Ты можешь (.*)",
        (
            "Почему вы решили что я не могу %1?",
            "Если бы я мог %1, тогда что?",
            "Почему вы решили спросить меня, могу ли я %1?",
        ),
    ),
    (
        r"Я могу (.*)",
        (
            "Может вы и не хотите %1.",
            "А вы хотите иметь возможность %1?",
            "Если бы вы могли %1, вы бы это сделали?",
        ),
    ),
    (
        r"Ты (.*)", 
        (
            "Почему вы думаете что я %1?",
            "Вам нравится думать что я %1?",
            "Возможно, вам бы хотелось чтобы я был %1.",
            "Может быть вы на самом деле думаете это про себя?",
        ),
    ),
    (
        r"Ты (.*)", 
        (
            "Почему вы думаете что я %1?",
            "Что заставляет вас думать что я %1?",
            "Мы говорим про меня или про вас?",
        ),
    ),
    (
        r"Я не (.*)", 
        ("Вы точно не %1?", "Почему вы не %1?", "Вы бы хотели %1?"),
    ),
    (
        r"Я чувствую (.*)",
        (
            "Хорошо, расскажи мне поподробнее о том что вы чувствуете.",
            "Вы часто чувствуете %1?",
            "Когда вы обычно чувствуете %1?", 
            "Когда вы чувствуете %1, что вы обычно делаете?",
        ),
    ),
    (
        r"У меня есть (.*)",
        (
            "Почему вы решили рассказать мне что у вас есть  %1?",
            "У вас точно есть %1?",
            "Хорошо. Если у вас есть %1, что вы будете делать дальше?",
        ),
    ),
    (
        r"Я буду (.*)",
        (
            "Объясни, пожалуйста, почему вы будете %1?",
            "Почему вы будете %1?",
        ),
    ),
    (
        r"Есть ли(.*)",
        (
            "Как вы сами думаете, есть ли %1?",
            "Вполне вероятно что есть %1.", 
            "Хотели бы вы чтобы был %1?",
        ),
    ),
    (
        r"Мой (.*)",
        (
            "Понятно. Ваш %1.",
            "Почему вы решили рассказать мне что ваш %1?",
            "Когда ваш %1, как вы чувствуете себя?",
        ),
    ),
    (
        r"Ты (.*)",
        (
            "Вы все-таки хотите обсуждать вас, а не меня.",
            "Почему вы сказали это про меня?",
            "Почему вы хотите знать, являюсь ли я %1?",
        ),
    ),
    (r"Почему (.*)", ("Почему бы вам не рассказать мне почему %1?", "Почему вы думаете %1?")),
    (
        r"Я хочу  (.*)",
        (
            "Что бы для вас значило если бы вы получили %1?",
            "Почему вы хотите %1?",
            "Что бы вы сделали если бы вы получили %1?",
            "Если бы вы получили %1, что бы вы тогда сделали?",
        ),
    ),
    (
        r"(.*) мама(.*)",
        (
            "Расскажите мне побольше про свою маму.",
            "Какие у вас были отношения с матерью?",
            "Что вы чувствуете по отношению к своей маме?",
            "Как бы вы соединили это с тем что вы чувствуете сегодня?",
            "Хорошие семейные отношения полезны для нас.",
        ),
    ),
    (
        r"(.*) папа(.*)",
        (
            "Расскажите мне поподробнее про своего отца.",
            "Какие чувства вызывает у вас отец?",
            "Как вы чувствуете по поводу своего отца?",
            "Как бы вы соединилм свои отношения с отцом с тем что вы чувствуете сегодня?",
            "Вам сложно показывать чувства перед своей семьей?",
        ),
    ),
    (
        r"(.*) ребенком(.*)", 
        (
            "У вас были близкие друзья когда вы был ребенком?",
            "Какое у вас любимое детское воспоминание?",
            "Вы помните какие-либо сны или кошмары из вашего детства?",
            "Вас дразнили другие дети?",
            "Как бы вы соединили свое детство с тем как вы себя сейчас чувствуете?",
        ),
    ),
    (
        r"(.*)\?",
        (
            "Почему вы это спрашиваешь?",
            "Скажи, вы бы могли сами ответить на этот вопрос?",
            "Возможно, ответ лежит в вас ?",
            "Почему бы вам не сказать мне?",
        ),
    ),
    (
        r"Пока",
        (
            "Спасибо, что вы побеседовали со мной.",
            "До свидания.",
            "Спасибо, с вас 2500 рублей. Приятного дня! Шутка)",
        ),
    ),
    (
        r"(.*)",
        (
            "Пожалуйста, расскажите поподробнее.",
            "Давайте немного сменим тему... Расскажите мне про свою семью.",
            "Можете рассказать поподробнее?",
            "Почему вы говорите что %1?",
            "Понятно.",
            "Звучит интересно.А поподробнее",
            "Ясно. Что вам это говорит?",
            "Какие это вызывает чувства в вас?",
            "Что вы чувствуете когда вы это говорите?",
        ),
    ),
)

psy_chatbot = Chat(pairs, reflections)


def psy_chat(string):

    ans = psy_chatbot.respond(string) 
    return ans




