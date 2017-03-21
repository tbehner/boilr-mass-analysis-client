venv:
	virtualenv venv
	. ./venv/bin/activate && pip install -r requirements.txt

image: venv
	docker build -t mass_system_{{AnalysisName | toLower}} .

.PHONY: clean
clean: 
	rm -rf venv
