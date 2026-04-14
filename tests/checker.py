import json
import sys
import re
import os

def check_code(code):
    # Remove lines that start with # (comments)
    code_no_comments = "\n".join([line for line in code.split("\n") if not line.strip().startswith("#")])
    # Also strip out spaces for easier regex searches on basic syntax
    compressed_code = code_no_comments.replace(" ", "")

    # 1. Imports
    if not re.search(r'import\s+pandas\s+as\s+pd|import\s+pandas', code_no_comments):
        print("FAIL: pandas not imported")
        return False
        
    if not re.search(r'from\s+sklearn\.linear_model\s+import\s+LinearRegression|import\s+sklearn', code_no_comments):
        print("FAIL: LinearRegression not imported")
        return False

    # 2. Drop NA correctly
    if "df=df.dropna()" not in compressed_code and "df.dropna(inplace=True)" not in compressed_code:
        print("FAIL: Data null values not handled permanently (missed inplace=True or reassignment to df)")
        return False

    # 3. Features vs Targets correctly parsed
    if "X=df[['Scores']]" in compressed_code or "X=df['Scores']" in compressed_code or "y=df['Hours']" in compressed_code or "y=df[['Hours']]" in compressed_code:
        print("FAIL: X and y variables are still swapped or predicted incorrectly.")
        return False
        
    if not ("X=df[['Hours']]" in compressed_code or "X=pd.DataFrame(df['Hours'])" in compressed_code):
        # Additional broad check to ensure they selected hours properly
        pass

    if not ("y=df['Scores']" in compressed_code or "y=df[['Scores']]" in compressed_code):
        # We don't necessarily hard-fail if there's other valid pandas syntax
        pass

    # 4. Correct plotting prediction
    if "model.predict(y)" in compressed_code:
        print("FAIL: The visualization function is still feeding 'y' to the model instead of 'X'")
        return False
        
    if "model.predict(X)" not in compressed_code:
        print("FAIL: Visualization should plot model.predict(X) to draw the regression line")
        return False

    # 5. Model Initialization
    if "model=LinearRegression()" not in compressed_code:
        print("FAIL: LinearRegression() is not properly assigned to the 'model' variable")
        return False

    # 6. Missing URL
    if "url=" not in compressed_code or "url=..." in compressed_code:
        print("FAIL: url was not properly defined.")
        return False

    # 7. Wrong training verb
    if "model.train(" in compressed_code:
        print("FAIL: model.train() focuses on the wrong vocabulary. Use the scikit-learn standard training function.")
        return False
        
    if "model.fit(" not in compressed_code:
        print("FAIL: model.fit() was not used to train the model with the dataset features and target.")
        return False

    # 8. Scatter plotting
    if "plt.scatter(" not in compressed_code:
        print("FAIL: plt.scatter() was incorrectly replaced with plt.plot() for displaying actual data.")
        return False

    return True

def main():
    filepath = os.path.join(os.path.dirname(__file__), "..", "devsphere_easy_challenge.ipynb")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            notebook = json.load(f)
    except FileNotFoundError:
        print("FAIL: devsphere_easy_challenge.ipynb not found. Did you delete or rename the notebook file?")
        sys.exit(1)
    except Exception as e:
        print(f"FAIL: Unable to read notebook. Is the JSON valid? Error: {e}")
        sys.exit(1)
        
    code_cells = [cell['source'] for cell in notebook.get('cells', []) if cell.get('cell_type') == 'code']
    
    # Reassemble all the cell lines into a unified string
    code = ""
    for cell in code_cells:
        for line in cell:
            code += line
        code += "\n"
        
    if check_code(code):
        print("PASS")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
