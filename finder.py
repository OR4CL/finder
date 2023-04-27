class File:


    @staticmethod
    def search_file(file_name, search_path="/"):
        import os
        """Recherche un fichier par son nom dans le système de fichiers"""
        matches = []
        for root, dirnames, filenames in os.walk(search_path):
            for filename in filenames:
                if filename == file_name:
                    matches.append(os.path.join(root, filename))
        result = print("Le fichier à été trouvé dans le/les chemins suivant :\n",'\n'.join(matches))
        return result

File.search_file("calculatrice.py")
