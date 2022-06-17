echo "################################"
echo "Running Tests.."
echo "################################"

echo "Running Test 1"
start=$(date +%s%N | cut -b1-13)
test1Output=$(cat sift-input-1.txt | python3 ./sift.py)
end=$(date +%s%N | cut -b1-13)
runtime=$(echo "$end - $start" | bc -l)
test1ExpectedOutput=$(cat ./sift-expected-output-1.txt)

if [ "$test1Output" = "$test1ExpectedOutput" ]; then
  echo "test 1 passed in ${runtime} milliseconds"
else
  echo "test 1 failed in ${runtime} milliseconds"
fi

echo "################################"
echo "Running Test 2"
start=$(date +%s%N | cut -b1-13)
test2Output=$(cat sift-input-2.txt | python3 ./sift.py)
end=$(date +%s%N | cut -b1-13)
runtime=$(echo "$end - $start" | bc -l)
test2ExpectedOutput=$(cat ./sift-expected-output-2.txt)

if [ "$test2Output" = "$test2ExpectedOutput" ]; then
  echo "test 2 passed in ${runtime} milliseconds"
else
  echo "test 2 failed in ${runtime} milliseconds"
fi
