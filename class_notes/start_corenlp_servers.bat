@echo off
echo starting english, chinese corenlp servers and ner servers
rem English corenlp server
start "English NLP Server" /d stanford-corenlp-full-2017-06-09 java -Xmx4g -cp .\* edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 2002 -timeout 15000

rem Chinese corenlp server
start "Chinese NLP Server" /d stanford-corenlp-full-2017-06-09 java -Xmx4g -cp .\* edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-chinese.properties -port 2003 -timeout 15000
