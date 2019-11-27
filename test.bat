python Main.py < ./tests/teste01.txt > ./tests/results.txt
python Main.py < ./tests/teste02.txt >> ./tests/results.txt
python Main.py < ./tests/teste03.txt >> ./tests/results.txt
python Main.py < ./tests/teste04.txt >> ./tests/results.txt
python Main.py < ./tests/teste05.txt >> ./tests/results.txt
python Main.py < ./tests/teste06.txt >> ./tests/results.txt
python Main.py < ./tests/teste07.txt >> ./tests/results.txt
python Main.py < ./tests/teste08.txt >> ./tests/results.txt
python Main.py < ./tests/teste09.txt >> ./tests/results.txt
python Main.py < ./tests/teste10.txt >> ./tests/results.txt
cd tests
FC respostas.txt results.txt
cd ..