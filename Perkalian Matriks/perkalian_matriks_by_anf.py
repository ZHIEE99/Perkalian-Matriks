import streamlit as st
import numpy as np

def multiply_matrices(matrix_a, matrix_b):
    """Mengalikan dua matriks."""
    try:
        result = np.dot(matrix_a, matrix_b)
        return result
    except ValueError as e:
        st.error(f"Error dalam perkalian matriks: {e}")
        return None

def get_matrix_input(key_suffix, rows, cols):
    """Mendapatkan input matriks dari pengguna."""
    matrix = []
    # Ensure rows and cols are integers for range function
    rows = int(rows)
    cols = int(cols)
    for r in range(rows):
        # Create columns dynamically for each row to align inputs
        cols_input = st.columns(cols)
        row_values = []
        for c in range(cols):
            # Use a unique key for each number_input to avoid duplicate key errors
            # The value is initialized to 0.0 to ensure it's always a float
            value = cols_input[c].number_input(f"Baris {r+1}, Kolom {c+1}", value=0.0, key=f"matrix_{key_suffix}_{r}_{c}")
            row_values.append(float(value))
        matrix.append(row_values)
    # Check if matrix is empty, return None if so to avoid numpy errors
    if not matrix:
        return None
    return np.array(matrix)

# Set the page configuration for a wider layout
st.set_page_config(layout="centered")

st.title("Kalkulator Perkalian Matriks")

st.write("""
Gunakan kalkulator ini untuk mengalikan dua matriks.
Pastikan jumlah kolom Matriks A sama dengan jumlah baris Matriks B.
""")

st.subheader("Matriks A")
# Use columns for better layout of dimension inputs
col1, col2 = st.columns(2)
with col1:
    rows_a = st.number_input("Jumlah Baris Matriks A", min_value=1, value=2, step=1, key="rows_a")
with col2:
    cols_a = st.number_input("Jumlah Kolom Matriks A", min_value=1, value=2, step=1, key="cols_a")

st.write("Masukkan elemen untuk Matriks A:")
# Get matrix input from the user
matrix_a_input = get_matrix_input("A", rows_a, cols_a)

st.subheader("Matriks B")
col3, col4 = st.columns(2)
with col3:
    rows_b = st.number_input("Jumlah Baris Matriks B", min_value=1, value=2, step=1, key="rows_b")
with col4:
    cols_b = st.number_input("Jumlah Kolom Matriks B", min_value=1, value=2, step=1, key="cols_b")

st.write("Masukkan elemen untuk Matriks B:")
matrix_b_input = get_matrix_input("B", rows_b, cols_b)

st.markdown("---")

# Button to trigger the calculation
if st.button("Hitung Perkalian"):
    # Validate matrix dimensions for multiplication
    if cols_a != rows_b:
        st.error("Untuk perkalian matriks, jumlah kolom Matriks A harus sama dengan jumlah baris Matriks B.")
    # Ensure both matrices have been input correctly
    elif matrix_a_input is not None and matrix_b_input is not None:
        result_matrix = multiply_matrices(matrix_a_input, matrix_b_input)
        if result_matrix is not None:
            st.subheader("Hasil Perkalian Matriks (A x B):")
            st.success("Perhitungan berhasil!")
            # Display the result using st.dataframe for a nice table format
            st.dataframe(result_matrix)
    else:
        st.warning("Mohon lengkapi semua input matriks dengan angka.")

st.markdown("---")
st.write("Dibuat dengan ❤️ oleh program Python")
