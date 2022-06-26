f = open('rosalind_gc.txt', 'r')
# id_max = 'a'
def my_function(gc_content):
    g_content = 0
    c_content = 0
    for i in gc_content:
        if i =='G' : g_content = g_content +1
        if i =='C' : c_content = c_content +1
    h = g_content + c_content
    l = len(gc_content)
    t = (float(h)/float(l))
    return round(t*100, 6)    
# my_function('GGGGGGGGCCCCCCATATATA')
maxGCContent = 0
maxID = ""
tempID = ""
tempGCContent = ""
for idx, val in enumerate(f.readlines()):
    if(val.startswith(">")) :
        if(tempGCContent != "") :
            gcContent = my_function(''.join(tempGCContent.split()))
            tempGCContent = ""
            print tempID, gcContent
            if(gcContent > maxGCContent) :
                maxID = tempID
                maxGCContent = gcContent
            # print maxID, maxGCContent, "\n"
        tempID = val
    else:
        tempGCContent += val
if(tempGCContent != "") :
    gcContent = my_function(''.join(tempGCContent.split()))
    tempGCContent = ""
    if(gcContent > maxGCContent) :
        maxID = tempID
        maxGCContent = gcContent
maxID = maxID.replace(">","")
print maxID, maxGCContent    
