In this project, I created an application that securely processes data from any provided web URL, segments it into chunks, and stores it as vector embeddings in a local FAISS database. This setup enables fast and accurate retrieval of contextually relevant information without the need for external data transfers.

Key Features:

Embeddings: Leveraged Hugging Face's "all-MiniLM-L6-v2" model for creating efficient, high-quality embeddings.

LLM: Integrated the LLAMA 3.2 model to enhance contextual understanding.

Vector Storage: Utilized FAISS DB for optimized local storage and retrieval.

This approach ensures data remains in our environment, making it a secure solution for applications that require privacy and local processing.

![Screenshot 2024-11-04 at 6 33 30 PM](https://github.com/user-attachments/assets/19019c94-4e93-448e-bd12-a4f503110b50)
![Screenshot 2024-11-04 at 6 33 04 PM](https://github.com/user-attachments/assets/cb0731d0-bdbf-4650-b901-96af130b9462)


