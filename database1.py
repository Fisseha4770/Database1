class HorizontalMinitermGenerator:
    def __init__(self, predicates):
        self.predicates = predicates

    def generate_miniterms(self):
        miniterms = []
        for predicate in self.predicates:
            miniterm = []
            for key, value in predicate.items():
                miniterm.append(f"{key}={value}")
            miniterms.append(" AND ".join(miniterm))
        return miniterms

# Example usage:
predicates = [
    {"age": "30", "gender": "Male"},
    {"age": "25", "gender": "Female", "city": "New York"}
]

generator = HorizontalMinitermGenerator(predicates)
miniterms = generator.generate_miniterms()
for miniterm in miniterms:
    print(miniterm)