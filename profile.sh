python -m cProfile -s cumtime -o profile.prof start.py
python print_profile.py profile.prof
pyprof2calltree -i profile.prof -o callgrind.output

