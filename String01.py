

def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:
        s: str
    Returns:
        str: answer
    """
    s=s.title()
    return s
print(main("hello world"))