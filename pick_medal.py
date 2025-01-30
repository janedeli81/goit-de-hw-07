import random
from prefect import task, flow

# Завдання: випадково вибирає тип медалі
@task
def pick_medal():
    medals = ["Bronze", "Silver", "Gold"]
    chosen_medal = random.choice(medals)
    print(f"🎖 Вибрано медаль: {chosen_medal}")
    return chosen_medal

# Потік Prefect
@flow
def medal_selection_flow():
    medal = pick_medal()
    print(f"🏅 Обрана медаль: {medal}")

if __name__ == "__main__":
    medal_selection_flow()
