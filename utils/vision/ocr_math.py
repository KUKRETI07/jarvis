
           # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 


# # # vision/ocr_math.py
# # import pytesseract
# # pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Dell\Downloads\tesseract-ocr-w64-setup-5.5.0.20241111.exe"
# # import cv2
# # import pytesseract            # C:\Program Files\Tesseract-OCR
# # import re
# # import sympy as sp

# # # Make sure Tesseract is installed and added to PATH
# # # Windows example (only if not already set):
# # # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # def capture_math_image():
# #     cap = cv2.VideoCapture(0)
# #     if not cap.isOpened():
# #         print("Camera not found")
# #         return None

# #     print("Show me the equation. Press 's' to scan.")
# #     while True:
# #         ret, frame = cap.read()
# #         if not ret:
# #             continue
        
# #         cv2.imshow("Jarvis - Math Scanner", frame)
# #         if cv2.waitKey(1) & 0xFF == ord('s'):
# #             break

# #     cap.release()
# #     cv2.destroyAllWindows()
# #     return frame

# # def extract_text_from_image(image):
# #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #     text = pytesseract.image_to_string(gray)
# #     return text.strip()

# # def solve_math_expression(text):
# #     # Extract valid math using regex (filter noise)
# #     expression = re.findall(r'[-+*/^()x0-9.]+', text.replace(' ', ''))
# #     if not expression:
# #         return "Sorry boss, I couldn't extract a valid math expression."
    
# #     expr = ''.join(expression)
# #     try:
# #         x = sp.Symbol('x')
# #         result = sp.sympify(expr)
# #         simplified = sp.simplify(result)
# #         return f"The solution to {expr} is {simplified}"
# #     except Exception as e:
# #         return f"Sorry, I couldn't solve it due to an error: {e}"

# # def detect_and_solve_math():
# #     image = capture_math_image()
# #     if image is None:
# #         return "No image captured."

# #     raw_text = extract_text_from_image(image)
# #     print("Detected Text:", raw_text)
# #     return solve_math_expression(raw_text)


# import base64
# import requests
# import cv2
# from voice.speak import speak  # Optional: Your Jarvis speak module

# # Replace with your real MathPix credentials
# APP_ID = "your_app_id_here"
# APP_KEY = "K82818891888957"

# def capture_equation_image(save_path="equation.jpg"):
#     cam = cv2.VideoCapture(0)
#     print(" Press 's' to scan the equation or 'q' to quit.")
#     while True:
#         ret, frame = cam.read()
#         cv2.imshow("Show the equation to camera", frame)
#         key = cv2.waitKey(1)
#         if key == ord('s'):
#             cv2.imwrite(save_path, frame)
#             break
#         elif key == ord('q'):
#             cam.release()
#             cv2.destroyAllWindows()
#             return None
#     cam.release()
#     cv2.destroyAllWindows()
#     return save_path

# def solve_math_with_mathpix(image_path):
#     with open(image_path, "rb") as image_file:
#         image_data = base64.b64encode(image_file.read()).decode()

#     headers = {
#     "app_id": "",                      
#     "app_key": "",                     
#     "Authorization": "K82818891888957",  
#     "Content-type": "application/json"
#     }


#     payload = {
#         "src": f"data:image/jpg;base64,{image_data}",
#         "formats": ["text", "data", "latex_simplified"],
#         "ocr": ["math", "text"]
#     }

#     response = requests.post("https://api.mathpix.com/v3/text", json=payload, headers=headers)
#     data = response.json()

#     if "text" in data:
#         extracted = data["text"]
#         print(" Extracted Text:", extracted)
#         speak(f"The solution is: {extracted}")
#         return extracted
#     else:
#         error = data.get("error", "Unknown error.")
#         print(" Error:", error)
#         speak("Sorry boss, I couldn't read the equation.")
#         return None


# import cv2
# import os
# import matplotlib.pyplot as plt
# import easyocr

# IMAGE_PATH = "equation.jpg"

# # === Display image using matplotlib ===
# def show_image(frame):
#     plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     plt.title("Show the equation - Press 'S' to scan or 'Q' to quit")
#     plt.axis('off')
#     plt.show(block=False)
#     plt.pause(1)
#     plt.close()

# # === Capture image from camera ===
# def capture_equation_image(filename=IMAGE_PATH):
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Could not open camera.")
#         return None

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             continue

#         show_image(frame)

#         key = input(" Press 's' to scan, or 'q' to quit: ").lower()

#         if key == 's':
#             cv2.imwrite(filename, frame)
#             print(f" Equation saved to {filename}")
#             cap.release()
#             return filename
#         elif key == 'q':
#             print(" Scan cancelled.")
#             cap.release()
#             return None

# # === Solve equation using EasyOCR ===
# def solve_math_with_easyocr(image_path):
#     reader = easyocr.Reader(['en'], gpu=False)
#     print(" Reading equation...")

#     try:
#         result = reader.readtext(image_path)
#         if result:
#             equation_text = ' '.join([text for (_, text, _) in result])
#             print("Detected equation:", equation_text)
#             return f"The equation is: {equation_text}"
#         else:
#             print(" No text found.")
#             return "Sorry boss, I couldn't read the equation."
#     except Exception as e:
#         print(" OCR error:", e)
#         return "Sorry boss, something went wrong while reading the equation."
# 



import cv2
import easyocr
from sympy import symbols, Eq, solve
import re

IMAGE_PATH = "equation.jpg"

# === Step 1: Capture equation image ===
def capture_equation_image(filename=IMAGE_PATH):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print(" Could not open camera.")
        return None

    print(" Show the math equation. Press 'S' to scan or 'Q' to cancel.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print(" Frame not received.")
            continue

        cv2.imshow(" JARVIS MATH SCANNER", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            cv2.imwrite(filename, frame)
            print(f" Equation saved to {filename}")
            cap.release()
            cv2.destroyAllWindows()
            return filename

        elif key == ord('q'):
            print(" Scan cancelled.")
            cap.release()
            cv2.destroyAllWindows()
            return None

# === Step 2: Solve math using EasyOCR + SymPy ===
def solve_math_with_easyocr(image_path):
    reader = easyocr.Reader(['en'], gpu=False)
    print(" Reading equation...")

    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = reader.readtext(gray)

        if not result:
            return "Sorry boss, I couldn't read the equation."

        # Extract and clean OCR text
        raw_text = ' '.join([item[1] for item in result])
        print(f"[OCR Raw]: {raw_text}")

        equation_text = raw_text.replace('−', '-').replace('–', '-')
        equation_text = equation_text.replace('×', '*').replace('÷', '/')
        equation_text = equation_text.replace(' ', '')

        # Fix common misread letters
        equation_text = re.sub(r'\bi\b', 'x', equation_text)
        equation_text = equation_text.replace('I', 'x').replace('l', 'x').replace('7', 'x')


        print(f"[Corrected]: {equation_text}")

        if '=' not in equation_text:
            return f"I detected: {equation_text}, but couldn't find '=' to solve."

        lhs, rhs = equation_text.split('=')

        # Create and solve the equation
        x = symbols('x')
        equation = Eq(eval(lhs), eval(rhs))
        solution = solve(equation, x)

        if solution:
            return f"The solution is: x = {solution[0]}"
        else:
            return "Sorry boss, I couldn't solve the equation."

    except Exception as e:
        import traceback
        traceback.print_exc()
        return "Sorry boss, something went wrong while reading the equation."




