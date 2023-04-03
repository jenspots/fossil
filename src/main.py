from dotenv import load_dotenv
from src.scheduler import Scheduler

if __name__ == "__main__":
    load_dotenv()
    Scheduler().run()
