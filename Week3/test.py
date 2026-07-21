    def retry(max_attempts=3):          # layer 1: takes the decorator's OWN arguments
    def decorator(func):            # layer 2: takes the function being decorated
        @wraps(func)
        def wrapper(*args, **kwargs):   # layer 3: the actual call
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        raise
        return wrapper
    return decorator
@retry(max_attempts=3)
def call_api():
    ...