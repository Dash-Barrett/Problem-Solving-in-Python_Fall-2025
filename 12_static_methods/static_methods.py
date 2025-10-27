class PathUtils:
    @staticmethod
    def get_extension(filename):
        """Return a file extension (including the dot)"""
        return filename[filename.rfind("."):] if "." in filename else ""
    
    # TODO
    @staticmethod
    def get_directory(path):
        """Returning the directory path without the file name"""
        pass
    @staticmethod
    def get_basename(path):
        """Return the file name from the directory path"""
        pass

# Use the class method
print(PathUtils.get_extension("image.img"))
print(PathUtils.get_extension("1.txt"))
print(PathUtils.get_extension("image"))