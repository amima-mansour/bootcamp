class Evaluator:
    def zip_evaluate(coeffs, words):
        if len(coeffs) != len(words):
            return (-1)
        result = 0
        for a, b in zip(words, coeffs):
            result += len(a) * b
        return result

    def enumerate_evaluate(coeffs, words):
        if len(coeffs) != len(words):
            return (-1)
        result = 0
        for i, word in enumerate(words):
            result += len(word) * coeffs[i]
        return (result)


