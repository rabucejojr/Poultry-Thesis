# Setting up Crontab for Automation

Crontab is a utility in Unix-like operating systems that allows users to schedule tasks to run periodically at fixed times, dates, or intervals. This README provides instructions on setting up Crontab for automating tasks, specifically for scheduling Python scripts to run at startup.

## For this project:

Use the following command:

To execute file every boot and with 5 minutes interval present in the code:
```bash
@reboot python3 /home/admin/Desktop/Poultry-Thesis/poultry_hardware_controller.py
```

To execute file every 5 minutes and the delay be removed on the code:
```bash
*/5 * * * * python3 /home/admin/Desktop/Poultry-Thesis/poultry_hardware_controller.py
```


For autofeeder function:

```bash
0 8 * * * python3 /home/admin/Desktop/Poultry-Thesis/auto-feeder.py
0 13 * * * python3 /home/admin/Desktop/Poultry-Thesis/auto-feeder.py
```

## List Existing Cron Jobs

To view a list of existing cron jobs, use the following command:

```bash
crontab -l
```

## Edit Cron Jobs

To edit the list of cron jobs, use the following command:

```bash
crontab -e
```

## Remove Cron Jobs

To remove all cron jobs for the current user, use the following command:

```bash
crontab -r
```
