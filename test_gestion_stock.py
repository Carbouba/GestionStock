import sys
from io import StringIO
import os

# Redirect standard input to simulate user typing
def run_test(inputs, description):
    print(f"--- Running Test: {description} ---")
    
    # Backup original stdin/stdout
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    
    sys.stdin = StringIO(inputs)
    sys.stdout = StringIO()
    
    try:
        # Import dynamically to reset state if needed, but here we just run it
        # Since the script has a while True, we need to be careful.
        # Ideally, we would import the functions, but the script runs at top level.
        # We will execute the file content in a separate environment dictionary.
        
        with open("c:/Users/Boubacar/Mes_projets_code/GestionStock/GestionStock.py", "r", encoding="utf-8") as f:
            code = f.read()
        
        exec(code, {'__name__': '__main__'})
        
        output = sys.stdout.getvalue()
        print("✅ Test execution finished")
        return output
    except Exception as e:
        print(f"❌ Test failed with exception: {e}")
        return sys.stdout.getvalue()
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

# Scenario 1: Add stock, View stock, Quit
# Inputs: 
# 2 (Add) -> "Pomme" -> 50
# 1 (View)
# 4 (Quit)
print("Testing Add and View...")
if os.path.exists("stock.txt"): os.remove("stock.txt") # Clean start
inputs_1 = "2\nPomme\n50\n1\n4\n"
output_1 = run_test(inputs_1, "Add Pomme (50) and Quit")
if "Pomme" in output_1 and "50" in output_1:
    print("SUCCESS: Pomme added correctly.")
else:
    print("FAILURE: Pomme not found in output.")
    print("Output was:", output_1)

# Scenario 2: Persistence check (Start, View, Quit)
# Expected: Pomme: 50 should be there from previous run
print("\nTesting Persistence...")
inputs_2 = "1\n4\n"
output_2 = run_test(inputs_2, "Start and View (Check Persistence)")
if "Pomme" in output_2 and "50" in output_2:
    print("SUCCESS: Persistence working, Pomme: 50 found.")
else:
    print("FAILURE: Persistence possibly failed.")
    print("Output type 2:", output_2)

# Scenario 3: Sell product (Sell 10 Pommes, View, Quit)
# Inputs:
# 3 (Sell) -> "Pomme" -> 10
# 1 (View)
# 4 (Quit)
print("\nTesting Sale...")
inputs_3 = "3\nPomme\n10\n1\n4\n"
output_3 = run_test(inputs_3, "Sell 10 Pommes")
if "Pomme" in output_3 and "40" in output_3:
    print("SUCCESS: Sale working, 40 Pommes remaining.")
else:
    print("FAILURE: Sale failed.")
    print("Output type 3:", output_3)

# Scenario 4: Error handling (Add negative, Sell too much)
# Inputs:
# 2 -> "Banane" -> -5 (error) -> 10 (ok)
# 3 -> "Banane" -> 20 (error) -> 5 (ok)
# 4
print("\nTesting Error Handling...")
inputs_4 = "2\nBanane\n-5\n10\n3\nBanane\n20\n5\n4\n"
output_4 = run_test(inputs_4, "Error Handling inputs")
if "Erreur" in output_4 and "Banane" in output_4 and "5" in output_4:
    print("SUCCESS: Error handling seems to work (found 'Erreur' and correct final state).")
else:
    print("FAILURE: Error handling test doubtful.")
    print("Output type 4:", output_4)
