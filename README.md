
---

# Flashcard Language Learning App

A beautifully designed Flashcard App built using Python and Tkinter to help users learn new languages efficiently. This project is part of my **#100DaysOfCode** challenge and showcases concepts like file handling, GUI development, and data persistence using Python.

## 📌 Features  
- **Dynamic Language Flashcards**: Displays French words and their English translations.  
- **Auto-Flip Functionality**: The flashcards flip automatically after 5 seconds to reveal the English meaning.  
- **Track Progress**:  
  - Users can mark words they already know.  
  - Progress is saved to a local file (`Words_to_learn.csv`), ensuring words marked as "known" won’t reappear in future sessions.  
- **Interactive GUI**: Includes buttons to interactively mark answers as correct or incorrect.

---

## 🛠️ Technologies Used  
- **Python**: Core programming language for logic and file operations.  
- **Tkinter**: For building a visually appealing graphical user interface.  
- **Pandas**: For efficient data handling and manipulation.  

---

## 🚀 How It Works  
1. **Start Learning**: The app randomly selects a German word from the dataset.  
2. **Flip the Card**: After 5 seconds, the card flips to reveal the English translation.  
3. **Track Known Words**: Click the ✅ button for words you know, and they are removed from the learning list.  
4. **Repeat Until Mastery**: Continue until all words are marked as "known."

---

## 🔑 Key Code Highlights  
### 1️⃣ Flip the Card Automatically  
```python  
def flip_card():  
    canvas.itemconfig(card_title, text="English", fill="white")  
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")  
    canvas.itemconfig(card_background, image=card_back)  
```  

### 2️⃣ Save Progress Dynamically  
```python  
def is_known():  
    to_learn.remove(current_card)  
    dat = pandas.DataFrame(to_learn)  
    dat.to_csv("data/Words_to_learn.csv", index=False)  
    next_card()  
```  

### 3️⃣ Handle Missing Files Gracefully  
```python  
try:  
    data = pandas.read_csv("data/Words_to_learn.csv")  
except FileNotFoundError:  
    original_data = pandas.read_csv("data/language.csv")  
    to_learn = original_data.to_dict(orient="records")  
else:  
    to_learn = data.to_dict(orient="records")  
```  

---

## 📝 Installation and Setup  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/flashcard-app.git  
   ```  
2. Navigate to the project folder:  
   ```bash  
   cd flashcard-app  
   ```  
3. Install required dependencies:  
   - Tkinter and Pandas come pre-installed with Python. If not, install them using:  
     ```bash  
     pip install pandas  
     ```  
4. Run the program:  
   ```bash  
   python flashcard_app.py  
   ```  

---

## 🎯 Key Takeaways  
- **File Handling**: How to handle missing or corrupted files gracefully.  
- **GUI Design**: Leveraging Tkinter to create a user-friendly interface.  
- **Data Management**: Persisting user progress using CSV files.

---

## 📸 Screenshots  
![image](https://github.com/user-attachments/assets/0ce10987-3694-4777-b494-d5a91e331661)

![image](https://github.com/user-attachments/assets/8547de79-13da-41cd-adee-421f619e6054)



---

## 💡 Future Enhancements  
- Add support for multiple languages.  
- Integrate with online language databases for dynamic word lists.  
- Add progress tracking with visual analytics.

---

## 🙌 Acknowledgments  
- Inspired by the **100 Days of Code Challenge** to push my programming skills.  
- Thanks to open datasets for providing resources for the flashcards.

---

### 🔗 Connect with Me  
If you’re inspired by this project or have feedback, feel free to connect:  
- **LinkedIn**: www.linkedin.com/in/het-patel-11s2004

---

Let me know if you'd like to tweak this or add specific details! 😊
