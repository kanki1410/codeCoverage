'''
Execute pylint checks for code PR's using Github actions.
Set threshold for passing: threshold ( presently set as 2 for testing in linter.yml)
'''
import argparse
import logging
import coverage

logging.getLogger().setLevel(logging.INFO)

parser = argparse.ArgumentParser(prog="COVERAGE")


logging.info('coverage Starting | '
             'Path: {} | '
             'Threshold: {} '.format(path, threshold))

cov = coverage.Coverage()

parser.add_argument('-p',
                    '--path',
                    help='path to directory you want to run coverage | '
                         'Default: %(default)s | '
                         'Type: %(type)s ',
                    default='./src',
                    type=str)

parser.add_argument('-t',
                    '--threshold',
                    help='score threshold to fail coverage runner | '
                         'Default: %(default)s | '
                         'Type: %(type)s ',
                    default=70,
                    type=float)

args = parser.parse_args()
path = str(args.path)
logging.info(path)

cov.start()



cov.stop()
results = cov.save()
data = cov.sysinfo()
threshold = float(args.threshold)
logging.info(threshold)
logging.info(results)
logging.info(data)
final_score = results

if final_score < threshold:

    message = ('PyLint Failed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

    logging.error(message)
    raise Exception(message)

else:
    message = ('PyLint Passed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

    logging.info(message)

    exit(0)
