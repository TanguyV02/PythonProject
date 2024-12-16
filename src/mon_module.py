def ajouter(a, b):
    """
    Additionne deux nombres ou deux listes.

    Parameters:
    a, b (int, float, list, tuple): Les deux éléments à additionner.

    Returns:
    int, float, list, tuple: Résultat de l'addition.

    Raises:
    ValueError: Si les types ou tailles ne sont pas compatibles.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)) and len(a) == len(b):
        return type(a)(x + y for x, y in zip(a, b))
    else:
        raise ValueError("Les types ne sont pas compatibles ou les dimensions ne correspondent pas.")
