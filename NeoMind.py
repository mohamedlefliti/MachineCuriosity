class EmergingMind:
    def __init__(self):
        self.memory = {}
        self.curiosity_level = 1.0
        self.observations = []
        self.hypotheses = []
        self.report = ""

    def observe(self, phenomenon):
        print(f"👀 Observing: {phenomenon}")
        self.observations.append(phenomenon)
        self.ask_questions(phenomenon)

    def ask_questions(self, phenomenon):
        questions = [
            "Is this wave-like or particle-like behavior?",
            "Does observation affect the outcome?",
            "Can a particle be in more than one state?",
            "Does this behavior repeat?"
        ]
        print("🤔 Curiosity Questions:")
        for q in questions:
            print(f"- {q}")
        self.generate_hypothesis(phenomenon)

    def generate_hypothesis(self, phenomenon):
        if "double-slit" in phenomenon or "interference" in phenomenon:
            hypothesis = "The electron behaves like a wave when unobserved, and like a particle when observed"
        else:
            hypothesis = "No clear hypothesis yet"
        self.hypotheses.append(hypothesis)
        print(f"🧠 Initial Hypothesis: {hypothesis}")
        self.validate_hypothesis(hypothesis)
        self.update_memory(phenomenon, hypothesis)
        self.write_report()

    def validate_hypothesis(self, hypothesis):
        keywords = ["wave", "particle", "observed"]
        if all(word in hypothesis for word in keywords):
            print("✅ The explanation reflects known quantum behavior.")
        else:
            print("⚠️ The explanation is incomplete or needs review.")

    def update_memory(self, phenomenon, hypothesis):
        self.memory[phenomenon] = hypothesis

    def write_report(self):
        self.report = "📄 EmergingMind Report:\n"
        for obs, hyp in self.memory.items():
            self.report += f"\nObservation: {obs}\n"
            self.report += f"Analysis: {hyp}\n"
            self.report += "Conclusion: The phenomenon indicates quantum behavior dependent on observation\n"
        print(self.report)


# 🧪 Test run in the quantum mechanics scenario
mind = EmergingMind()
mind.observe("In the double-slit experiment, electrons display an interference pattern when unobserved, and behave like particles when observed")
