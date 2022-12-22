import datetime
import time
import subprocess


def run_program(program_name):
    subprocess.run(["python3",program_name])

if __name__ == '__main__':
  # Set the timezone to EST
  est = datetime.timezone(datetime.timedelta(hours=-5))

  # Define the schedule
  schedule = [
    (16, 0, 0, "/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program1.py"),
    (16, 0, 40, "/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program2.py"),
    (16, 1, 30, "/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program3.py"),
    (16, 2, 5, "/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program4.py"),
    (16, 2, 30, "/Users/alexandergursky/Local_Repository/Python_General/Python_Script/Bots/program5.py")
  ]

  # Run the programs according to the schedule
  while True:
    now = datetime.datetime.now(est)
    hour = now.hour
    minute = now.minute
    second = now.second
    for (scheduled_hour, scheduled_minute, scheduled_second, program_name) in schedule:
      if scheduled_hour == hour and scheduled_minute == minute and scheduled_second == second:
        run_program(program_name)
    time.sleep(1)
