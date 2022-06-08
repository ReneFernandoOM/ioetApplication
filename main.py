from src import calculator
from src.errors import ExpectedError 

if __name__ == '__main__':
    try:
        calculator.run()
    except ExpectedError as e:
        print(e)
    # except Exception as e:
    #     print(f"Unexpected error: {e}")