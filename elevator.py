from pathlib import Path

from prefect import flow, task
from prefect.task_runners import ThreadPoolTaskRunner
from prefect.client.schemas.schedules import CronSchedule
import time

@task(task_run_name="Stop at {floor}")
def stop_at_floor(floor):
    print(f"elevator moving to floor {floor}")
    time.sleep(floor)
    print(f"elevator stops on floor {floor}")

@flow(task_runner=ThreadPoolTaskRunner(max_workers=10), log_prints=True)
def elevator_flow():
    floors = []

    for floor in range(5, 0, -1):
        floors.append(stop_at_floor.submit(floor))

    results = [floor.result() for floor in floors]

if __name__ == "__main__":
    deployment_name = "_".join([Path(__file__).stem, "test", "deployment"])
    schedules = [CronSchedule(cron="00 * * * *", timezone="Europe/Tallinn")]
    elevator_flow.serve(
        name=deployment_name,
        schedules=schedules,
    )