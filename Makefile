.PHONY: all test analyze figures clean human

all: test analyze figures

test:
	python3 tests/test_agreement.py

analyze:
	python3 src/analyze.py

figures:
	python3 src/figures.py

human:
	python3 src/human_sheet.py --make

clean:
	rm -f results/agreement_report.md results/disagreements.md results/scores_long.csv
	rm -f results/figures/*.png
