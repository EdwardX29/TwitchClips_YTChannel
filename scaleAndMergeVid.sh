iSegment=""
temp=""
filter=""
counter=0

temp+="-i intro3.mp4 "
filter+="[$counter:v]scale=1920x1080[v$counter];"
counter=$((counter+1))

for file in "clips/"*;
do 
    temp+="-i $file "
    filter+="[$counter:v]scale=1920x1080[v$counter];"
    counter=$((counter+1))
done

temp+="-i outro3.mp4 "
filter+="[$counter:v]scale=1920x1080[v$counter];"



counter=0
for file in "clips/"*;
do
    filter+="[v$counter] [$counter:a] "
    counter=$((counter+1))
done

filter+="[v$counter] [$counter:a] "
counter=$((counter+1))
filter+="[v$counter] [$counter:a] "
counter=$((counter+1))


filter+="concat=n=$counter:v=1:a=1 [vv] [aa]"

command='ffmpeg $temp -filter_complex "$filter" -map "[vv]" -map "[aa]"  mergedVideo2.mp4'

echo $command
eval $command