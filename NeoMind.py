import math

class EmergingMind:
    def __init__(self):
        self.memory = []
        self.keywords = ["wave", "particle", "observation", "interference", "electron"]
        self.rules = {
            "wave–particle duality": True,
            "observation alters behavior": True,
            "interference implies wave behavior": True
        }

    def observe(self, description):
        print(f"\n📘 Observation received:\n{description}")
        return description

    def generate_questions(self, description):
        questions = []
        desc = description.lower()
        if "interference" in desc:
            questions.append("Is this wave-like or particle-like behavior?")
        if "observed" in desc or "observation" in desc:
            questions.append("Does observation affect the outcome?")
        if "electron" in desc or "particle" in desc:
            questions.append("Can a particle be in more than one state?")
        questions.append("Is this behavior repeatable?")
        return questions

    def generate_hypothesis(self, description):
        desc = description.lower()
        if "interference" in desc and "observed" in desc:
            return "An electron behaves like a wave when unobserved, and like a particle when observed."
        elif "interference" in desc:
            return "The phenomenon suggests wave-like behavior."
        elif "observed" in desc:
            return "Observation may influence particle behavior."
        elif "stone" in desc and "flies" in desc and "water" in desc:
            return "The stone defies gravity when dropped into water."  # غير منطقي
        else:
            return "Further observation is required to form a hypothesis."

    def infer_strength(self, d_t, d_A, c):
        try:
            Z_t = (d_t / d_A) + math.exp(c)
            return round(Z_t, 3)
        except ZeroDivisionError:
            return float('inf')

    def validate(self, Z_t):
        if Z_t < 1.5:
            return False  # فرضية ضعيفة أو غير منطقية
        elif Z_t >= 2.5:
            return True   # فرضية قوية ومنطقية
        else:
            return None   # محتملة، تحتاج مراجعة إضافية

    def record(self, observation, hypothesis, Z_t, valid):
        self.memory.append({
            "observation": observation,
            "hypothesis": hypothesis,
            "strength": Z_t,
            "valid": valid
        })

    def report(self, observation, questions, hypothesis, Z_t, valid):
        print("\n🧠 Reasoning Report:")
        print(f"- Observation: {observation}")
        print(f"- Questions: {questions}")
        print(f"- Hypothesis: {hypothesis}")
        print(f"- Inference Strength Z(t): {Z_t}")
        if valid is True:
            print("- Validated: ✅ Strong and logical")
        elif valid is False:
            print("- Validated: ❌ Weak or illogical")
        else:
            print("- Validated: 🤔 Needs further review")
        print(f"- Memory size: {len(self.memory)}")

    def reasoning_loop(self, description, d_t, d_A, c):
        obs = self.observe(description)
        questions = self.generate_questions(obs)
        hypothesis = self.generate_hypothesis(obs)
        Z_t = self.infer_strength(d_t, d_A, c)
        valid = self.validate(Z_t)
        self.record(obs, hypothesis, Z_t, valid)
        self.report(obs, questions, hypothesis, Z_t, valid)
agent = EmergingMind()

# مثال منطقي: تجربة الشق المزدوج
description1 = "In the double-slit experiment, electrons display an interference pattern when not observed, but behave like particles when observed."
agent.reasoning_loop(description1, d_t=80, d_A=50, c=0.3)

# مثال غير منطقي: حجر يطير في الماء
description2 = "When a stone is dropped into water, it flies into the air."
agent.reasoning_loop(description2, d_t=20, d_A=50, c=0.1)


description = "When an electron is dropped into vacuum, it stops moving completely."

# قيم منخفضة تعكس ضعف الملاحظة والمنطق
d_t = 10      # شدة الملاحظة
d_A = 50      # القيمة المرجعية
c = 0.05      # تأثير السياق

agent.reasoning_loop(description, d_t, d_A, c)

