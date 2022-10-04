import time
import threading
from threading import Lock

PRINT_LOCK = Lock()


def check_creds(username, password):
    # Stub to replace with authentication function
    if 0:
        with PRINT_LOCK:
            print(f"Found Credentials: {username}:{password}")
        return True
    else:
        return False


def main():
    start = time.perf_counter()
    creds_to_try = [["username", "test"] for _ in range(49)] + [
        ["username", "password"]
    ]
    number_of_threads = 10
    current_cred_idx = 0
    done = False

    while not done:
        threads = []
        for _ in range(number_of_threads):
            thread = threading.Thread(
                target=check_creds,
                args=creds_to_try[current_cred_idx],
                daemon=True,
            )
            thread.start()
            threads.append(thread)
            current_cred_idx += 1
            if current_cred_idx == len(creds_to_try):
                done = True
                break

        for thread in threads:
            thread.join()

    time_taken = round(time.perf_counter() - start)
    minutes, seconds = divmod(time_taken, 60)
    print(f"Done in: {minutes} minute(s), {seconds} second(s)")


if __name__ == "__main__":
    main()
