from pyats.easypy import run

# We want to run multiple tests as part of job
# Run job via commands: pyats run job aetest_job.py --testbed-file testbed.yaml

def main():
    run('aetest_eg.py')
    run('aetest_eg2.py')

