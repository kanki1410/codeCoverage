'''
Execute pylint checks for code PR's using Github actions.
Set threshold for passing: threshold ( presently set as 2 for testing in linter.yml)
'''
import argparse
import logging
import coverage
import test_main

logging.getLogger().setLevel(logging.INFO)

parser = argparse.ArgumentParser(prog="LINT")


parser.add_argument('-p',
                    '--path',
                    help='path to directory you want to run pylint | '
                         'Default: %(default)s | '
                         'Type: %(type)s ',
                    default='./src',
                    type=str)

parser.add_argument('-t',
                    '--threshold',
                    help='score threshold to fail pylint runner | '
                         'Default: %(default)s | '
                         'Type: %(type)s ',
                    default=7,
                    type=float)

args = parser.parse_args()
path = str(args.path)
threshold = float(args.threshold)

logging.info('PyLint Starting | '
             'Path: {} | '
             'Threshold: {} '.format(path, threshold))

cov = coverage.Coverage()
cov.start()
result = test_main.test_sauce_selection()
cov.stop()
final_score = results.linter.stats.global_note

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