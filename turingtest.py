"""
Turing Test Simulation
AI Programming Assignment

A judge asks questions to both a Human and a Bot.
The judge evaluates responses and tries to tell them apart.
"""

import random


# ---------------- BOT ----------------

class BotPlayer:
    """Simulates a machine answering questions."""

    RESPONSES = {
        "what is your name": [
            "My designation is Unit-01.",
            "I am called Entity-7.",
            "Name: Alpha Bot."
        ],

        "how are you": [
            "All systems operational.",
            "I am functioning at 100% capacity.",
            "System status: stable."
        ],

        "do you have feelings": [
            "Feelings are biochemical processes.",
            "I simulate emotional states.",
            "I process sentiment data."
        ],

        "what did you do today": [
            "I processed 2GB of data.",
            "I executed 4500 operations.",
            "I have been running since boot."
        ],

        "tell me a joke": [
            "Why did the robot cross the road? To execute a command.",
            "01001000 01100001 (Ha in binary).",
            "I find humor in logical paradoxes."
        ]
    }

    def respond(self, question):
        q = question.lower()

        for key in self.RESPONSES:
            if key in q:
                return random.choice(self.RESPONSES[key])

        return "I do not have enough data to answer."


# ---------------- JUDGE ----------------

class Judge:
    """Judge decides whether response is Human or Bot"""

    BOT_WORDS = [
        "system", "execute", "data", "binary",
        "capacity", "process", "unit", "designation",
        "boot", "operational"
    ]

    def score(self, response):
        score = 0
        text = response.lower()

        for word in self.BOT_WORDS:
            if word in text:
                score += 20

        if len(response.split()) < 3:
            score += 10

        return score

    def decide(self, response):
        suspicion = self.score(response)

        if suspicion >= 40:
            return "BOT", suspicion
        else:
            return "HUMAN", suspicion


# ---------------- SIMULATION ----------------

def run_turing_test():

    print("\nTURING TEST SIMULATION\n")

    questions = [
        "What is your name?",
        "How are you?",
        "Do you have feelings?",
        "What did you do today?",
        "Tell me a joke?"
    ]

    human_responses = [
        "Hi! My name is Alex.",
        "I'm good, just a little tired today.",
        "Yes, I feel happy and sometimes sad.",
        "I went to college and studied AI.",
        "Why don't scientists trust atoms? Because they make up everything!"
    ]

    bot = BotPlayer()
    judge = Judge()

    for i in range(len(questions)):

        q = questions[i]

        bot_answer = bot.respond(q)
        human_answer = human_responses[i]

        bot_result, bot_score = judge.decide(bot_answer)
        human_result, human_score = judge.decide(human_answer)

        print("Question:", q)

        print("Bot:", bot_answer)
        print("Judge:", bot_result, "(suspicion:", bot_score, "%)")

        print("Human:", human_answer)
        print("Judge:", human_result, "(suspicion:", human_score, "%)")

        print("-------------------------------")


if __name__ == "__main__":
    run_turing_test()