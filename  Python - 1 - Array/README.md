# Python for Data Science - 1: Array

## PYTHON - 1

---

### EX00 - BMI Calculator (NumPy vectorized math)

>> ### What you learn:
>> Converting Python lists into NumPy arrays unlocks **vectorized operations** — math
>> applied to every element at once in C speed, with no Python loops.
>>
>> ### Key concepts:
>> - `np.array(lst, dtype=float)` — typed, contiguous memory block
>> - Element-wise math: `arr_w / arr_h ** 2` (no loop needed)
>> - Boolean broadcasting: `arr > 26` → array of True/False
>> - `.tolist()` — converts NumPy scalars back to plain Python types
>>
>> ### The formula:
>> ```
>> BMI = weight (kg) / height (m)²
>> ```
>> | BMI range | Category |
>> |-----------|----------|
>> | < 18.5 | Underweight |
>> | 18.5 – 24.9 | Normal |
>> | 25 – 29.9 | Overweight |
>> | ≥ 30 | Obese |
>>
>> ### Loop vs vectorized — same result, very different speed:
>> ```python
>> # Plain Python (slow at scale)
>> bmi = [w / h**2 for h, w in zip(height, weight)]
>>
>> # NumPy vectorized (C speed, no Python loop)
>> bmi = (np.array(weight) / np.array(height) ** 2).tolist()
>> ```
>> At 10 million rows, the NumPy version is ~100x faster.
>>
>> ### Why `.tolist()` not `list()`:
>> `list(np_array)` gives `[np.float64(22.5), ...]` — NumPy scalar wrappers.
>> `.tolist()` gives `[22.5, ...]` — plain Python floats. Always use `.tolist()`.
>>
>> ### Error cases to handle:
>> - Both arguments must be `list`
>> - Same length (zip silently truncates otherwise)
>> - All elements must be `int` or `float`
>> - Height must be > 0 (division by zero)

---

### EX01 - 2D Array Slicing (NumPy shapes and slicing)

>> ### What you learn:
>> NumPy's `shape` attribute and **slicing syntax** are the backbone of data
>> manipulation. Every dataset you'll ever work with is essentially a 2D (or higher)
>> array being sliced.
>>
>> ### Key concepts:
>> - `arr.shape` → `(rows, cols)` tuple — fundamental to understanding your data
>> - `arr[start:end]` — row slicing (Python slice rules apply: negatives, omitted bounds)
>> - `ndim` — number of dimensions; 2D arrays have `ndim == 2`
>>
>> ### Shape explained:
>> ```python
>> family = [[1.80, 78.4],   # person 0: height, weight
>>           [2.15, 102.7],  # person 1
>>           [2.10, 98.5],   # person 2
>>           [1.88, 75.2]]   # person 3
>>
>> arr = np.array(family)
>> arr.shape  # → (4, 2)  — 4 rows, 2 columns
>> arr[0:2]   # → rows 0 and 1 → shape (2, 2)
>> arr[1:-2]  # → row 1 only (stop at 2nd from end) → shape (1, 2)
>> ```
>>
>> ### Slice rules recap:
>> ```python
>> arr[start:end]   # rows from start up to (not including) end
>> arr[:3]          # first 3 rows
>> arr[-1:]         # last row only
>> arr[1:-1]        # everything except first and last row
>> ```
>>
>> ### Why this matters:
>> In data science, slicing is how you split train/test sets, extract
>> batches, and inspect data samples — all without copying memory.

---

### EX02 - Loading Images (Images as NumPy arrays)

>> ### What you learn:
>> A digital image is just a 3D array: `(height, width, channels)`.
>> Understanding this representation is the entry point to all computer
>> vision work.
>>
>> ### Key concepts:
>> - PIL/Pillow `Image.open()` + `.convert('RGB')` — loads any image
>> - `np.array(img)` — converts PIL image to a NumPy array
>> - Shape `(H, W, 3)` — height × width × (R, G, B)
>> - `dtype=uint8` — pixel values are integers 0–255
>>
>> ### Image anatomy:
>> ```
>> arr.shape  →  (257, 450, 3)
>>              ────  ───  ─
>>              rows  cols  channels (R, G, B)
>>
>> arr[0, 0]  →  [19, 42, 83]   ← pixel at top-left (R=19, G=42, B=83)
>> arr[256, 449]  ← pixel at bottom-right
>> ```
>>
>> ### Accessing pixels:
>> ```python
>> arr[row, col]        # single pixel: [R, G, B]
>> arr[row, col, 0]     # just the Red value of that pixel
>> arr[:, :, 0]         # the entire Red channel (all rows, all cols)
>> arr[10:50, 20:80]    # a rectangular crop
>> ```
>>
>> ### Colour channel ranges:
>> - 0 = no contribution from that channel (dark)
>> - 255 = full contribution (bright)
>> - [255, 0, 0] = pure red | [0, 255, 0] = pure green | [0, 0, 255] = pure blue
>> - [255, 255, 255] = white | [0, 0, 0] = black

---

### EX03 - Zoom (Slicing + Grayscale conversion)

>> ### What you learn:
>> **Spatial slicing** on an image is just array slicing.
>> **Grayscale conversion** collapses 3 colour channels into 1 by averaging.
>>
>> ### Key concepts:
>> - `arr[200:600, 300:700]` — crop: rows 200–600, columns 300–700
>> - `.mean(axis=2, keepdims=True)` — average across channel axis
>> - `keepdims=True` preserves the 3rd dimension → shape `(H, W, 1)`
>> - `cmap='gray'` in matplotlib — renders single-channel data as greyscale
>>
>> ### How grayscale averaging works:
>> ```python
>> pixel = [120, 111, 132]          # R=120, G=111, B=132
>> grey  = (120 + 111 + 132) / 3   # = 121  (average)
>> # New pixel: [121, 121, 121]  — equal R, G, B = grey
>> ```
>>
>> ### Axis argument explained:
>> ```python
>> arr.shape      # (400, 400, 3)
>> arr.mean(axis=0)  # average across rows    → shape (400, 3)
>> arr.mean(axis=1)  # average across columns → shape (400, 3)
>> arr.mean(axis=2)  # average across channels → shape (400, 400)
>> arr.mean(axis=2, keepdims=True)  # → shape (400, 400, 1)  ← keeps dim
>> ```
>>
>> ### 2D slicing — cutting a rectangle from an image:
>> ```python
>> # 1D: one axis
>> lst[1:4]
>>
>> # 2D: two axes at once → [rows, cols]
>> arr[200:600, 300:700]   # rows 200–599, cols 300–699 → (400, 400, 3)
>> ```
>> In real life, these coordinates come from object detection — same syntax.
>>
>> ### axis= explained on a (2, 3, 3) array:
>> ```python
>> arr.mean(axis=0)  # collapse rows    → shape (3, 3)
>> arr.mean(axis=1)  # collapse cols    → shape (2, 3)
>> arr.mean(axis=2)  # collapse channels → shape (2, 3)  ← grayscale
>> ```
>> Rule: the axis you name is the one that disappears.
>>
>> ### Why keepdims=True matters:
>> ```python
>> mean = arr.mean(axis=2)               # shape (400, 400)
>> arr - mean                            # CRASH — can't broadcast (400,400,3) - (400,400)
>>
>> mean = arr.mean(axis=2, keepdims=True) # shape (400, 400, 1)
>> arr - mean                            # OK — 1 broadcasts against 3
>> ```
>> NumPy broadcasting: dimensions must match or be 1. keepdims=True keeps
>> the collapsed axis as 1 so math still works across the whole array.
>>
>> ### Why .astype(np.uint8):
>> ```python
>> arr.mean(axis=2).dtype   # float64 — values like 121.333...
>> # images expect integers 0–255 (uint8)
>> # also: uint8 = 1 byte/pixel vs float64 = 8 bytes/pixel → 8x less memory
>> ```
>>
>> ### Why [:, :, 0] before imshow:
>> ```python
>> zoomed.shape           # (400, 400, 1)
>> zoomed[:, :, 0].shape  # (400, 400)  ← drop the dim
>> # imshow accepts (H,W), (H,W,3), (H,W,4) — NOT (H,W,1)
>> ```
>> cmap='gray' maps low values → black, high → white.
>> Without it matplotlib uses viridis (default colormap) on single-channel data:
>> ```
>> viridis:   0 → dark blue/purple | 128 → green | 255 → yellow
>> cmap=gray: 0 → black            | 128 → grey  | 255 → white
>> ```
>> Same data, completely different display — only the colormap changes how
>> values are rendered. matplotlib doesn't read the variable name 'grey',
>> it just sees a 2D array of numbers and needs cmap='gray' to know the intent.
>>
>> ### Matplotlib scale display:
>> `plt.imshow()` automatically shows pixel-coordinate axes. This is the
>> "scale on x and y" the subject asks for — no extra code needed.

---

### EX04 - Rotate (Manual Transpose)

>> ### What you learn:
>> A **transpose** swaps rows and columns: `result[j][i] = original[i][j]`.
>> Implementing it manually (no library) forces you to understand exactly
>> what happens to array indices during a rotation.
>>
>> ### Key concepts:
>> - Shape before: `(rows, cols)` → shape after: `(cols, rows)`
>> - For a square array (400×400) the shape stays the same but pixels rotate
>> - The only way to do it without a library: nested indexing
>>
>> ### Manual transpose — the core idea:
>> ```python
>> original = [[1, 2, 3],   # shape (2, 3)
>>             [4, 5, 6]]
>>
>> # result[col][row] = original[row][col]
>> result  = [[1, 4],       # shape (3, 2)
>>            [2, 5],
>>            [3, 6]]
>> ```
>>
>> ### Implementation (no .T, no np.transpose):
>> ```python
>> rows, cols = arr.shape
>> result = np.array(
>>     [[arr[i, j] for i in range(rows)] for j in range(cols)]
>> )
>> ```
>> Outer loop: iterates new rows (old columns).
>> Inner loop: iterates new columns (old rows).
>>
>> ### What to NOT use (forbidden):
>> ```python
>> arr.T              # ← forbidden library shortcut
>> np.transpose(arr)  # ← forbidden
>> np.swapaxes(arr, 0, 1)  # ← forbidden
>> ```
>>
>> ### Visual effect:
>> A 90° clockwise rotation of the image — what was the top-left corner
>> becomes the top-right after transposing a square image.

---

### EX05 - Pimp My Image (Channel manipulation)

>> ### What you learn:
>> Colour filters work by **selectively zeroing out or rescaling channels**.
>> Each filter uses only restricted operators to force you to think about
>> what each operator actually does to the pixel data.
>>
>> ### Channel structure reminder:
>> ```
>> pixel = [R, G, B]  →  arr[:, :, 0]=R  arr[:, :, 1]=G  arr[:, :, 2]=B
>> ```
>>
>> ### The five filters explained:
>>
>> **Invert** (`=, +, -, *`): flip every value to its complement
>> ```python
>> result = 255 - array   # [100,150,200] → [155,105,55]
>> ```
>>
>> **Red** (`=, *`): keep R, zero G and B by multiplying by 0
>> ```python
>> result[:, :, 1] = result[:, :, 1] * 0   # G → 0
>> result[:, :, 2] = result[:, :, 2] * 0   # B → 0
>> ```
>>
>> **Green** (`=, -`): zero R and B by subtracting themselves (x - x = 0)
>> ```python
>> result[:, :, 0] = result[:, :, 0] - result[:, :, 0]  # R → 0
>> result[:, :, 2] = result[:, :, 2] - result[:, :, 2]  # B → 0
>> ```
>>
>> **Blue** (`=`): zero R and G by direct assignment
>> ```python
>> result[:, :, 0] = 0   # R → 0
>> result[:, :, 1] = 0   # G → 0
>> ```
>>
>> **Grey** (`=, /`): average the three channels using division
>> ```python
>> grey = array.astype(np.uint16).sum(axis=2, keepdims=True) / 3
>> result[:, :, :] = grey.astype(np.uint8)
>> ```
>> (`uint16` prevents overflow before dividing: 255+255+255=765 fits in uint16)
>>
>> ### Why uint8 overflow matters:
>> ```python
>> np.uint8(200) + np.uint8(100)  # = 44  ← WRONG! wraps around at 255
>> np.uint16(200) + np.uint16(100)  # = 300  ← correct
>> ```
>> Always upcast before summing channels.
>>
>> ### Lesson:
>> Understanding channel manipulation is the foundation of image
>> preprocessing in deep learning: normalisation, augmentation, and
>> colour-space conversion all work this way.
