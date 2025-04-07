# Misc. helper functions (parsing data, etc.)

def parse_tags_raw(tags_raw:str):
    tags = []
    seen = set() #sets cannot contain duplicates, so we can use this as a base for the list

    if not tags_raw.strip(): #if all tags are empty or just spaces, return empty list
        return tags
    
    for tag in tags_raw.split(","): #splits based on commas and parses
        if tag.strip(): #checks for emptiness/ws only
            tag = tag.strip().replace(" ", "_").lower() #formatting
            if tag not in tags: #checks for duplicates
                tags.append(tag) #appends formatted, non-duplicate tag to the list
    return tags #returns the formatted list with no duplicates

def normalize_name(name: str):
    return name.strip().lower()