from pathlib import Path



def load_mp3_files(path):
    """
    Input a path as a string or a path.
    Returns all mp3 files in a specified directory. This is returned as a list
    of paths. If an error occurs, a custom exception is raised detailing the problems 
    instead. Does not search subdirectories.
    """

    problems = ''
    
    if not path:
        problems += 'No path specified.'
        raise Exception(problems)
    
    path = Path(path)
    
    try:
        if path.is_dir():
            
            found_mp3s = []
            
            for file in path.iterdir():
                try:
                    
                    if not file.is_file():
                        continue
                    
                    if file.suffix.lower() == '.mp3':

                        found_mp3s.append(file)
                    
                except PermissionError:
                    continue
            
            return found_mp3s
        
        
        else:
            problems += 'Path is not a directory.'
            raise Exception(problems)
    
    except PermissionError:
        problems += 'Access denied. This may be a restricted or system folder.'
        raise PermissionError(problems)




def load_album_cover(path):
    """
    Returns an album cover. The album cover is the first JPEG file found in 
    the specified directory. Does not search subdirectories. Returns the file
    as a path. If no file is found, None is returned.
    """

    problems = ''
    
    if not path:
        problems += 'No path specified.'
        raise Exception(problems)
    
    path = Path(path)
    
    try:
        if path.is_dir():
        
            for file in path.iterdir():
                try:
                    
                    if not file.is_file():
                        continue
                    
                    if file.suffix.lower() in {'.jpg', '.jpeg'}:
                        return file
                
                except PermissionError:
                    continue
                
            return None
            
            
        else:
            problems += 'Path is not a directory.'
            raise Exception(problems)
    
    except PermissionError:
        problems += 'Access denied. This may be a restricted or system folder.'
        raise PermissionError(problems)