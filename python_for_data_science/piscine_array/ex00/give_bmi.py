#  les [] sur le return permettent de retourner une liste directement
#  la fonction zip parcours plusieurs iterateurs en une seule fois


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    take list of height and weight and return list of bmi(float or int)
    """
    if (len(height) != len(weight)):
        print("Error: length of height and weight should be same")
        return (1)
    return [w / h ** 2 for h, w in zip(height, weight)]       


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    take list of bmi and limit and return list of bool
    """
    return [b > limit for b in bmi]
