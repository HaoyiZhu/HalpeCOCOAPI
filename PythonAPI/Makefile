all:
    # install cocohalpetools locally
	python setup.py build_ext --inplace
	rm -rf build

install:
	# install cocohalpetools to the Python site-packages
	python setup.py build_ext
	python -m pip install ./
	rm -rf build