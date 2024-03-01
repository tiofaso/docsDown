import requests

# Read the file with the google docs ids
def sourceIds():
    with open('gdocsId.dat','r') as file:
        allIds = file.read()

    # Converting to vector
    allIds = allIds.split()

    return(allIds)

def downloGdocs(docId, outputFilename):
    # Making the URL for download
    downloadUrl = f"https://docs.google.com/document/d/{docId}/export?format=docx"
    
    response = requests.get(downloadUrl)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the content of the response to a file
        with open(f"{outputFilename}.docx", 'wb') as file:
            file.write(response.content)
        print(f"Document downloaded successfully as {outputFilename}")
    else:
        print("Failed to download document. Please check the document ID and your permissions. {e}")

def main():
    finalIds = sourceIds()

    # Simple flag
    count = 0

    # Download Gdocs files and wrinting them localy
    for singleId in finalIds:
        finalName = 'text-doc' + '_' + str(count)      
        downloGdocs(singleId,finalName)    
        count+=1

if __name__ == '__main__':
    main()