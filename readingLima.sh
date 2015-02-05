
#!/bin/bash
COUNTER=0
while [  $COUNTER -lt 1000 ]; do
    echo The counter is $COUNTER
    COUNTER=$(($COUNTER + 1))
    python twitterstream.py > output.txt& PID=$!; sleep 300; kill $PID
    python tweet_sentiment.py 'output.txt'    
 done
         

