from functools import wraps

def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise

        return wrapper
    return decorator