<div align="center">

# 🤖 Karel: Fill the World

### *Stanford CS106A — Karel the Robot*

</div>

---

## 📋 Assignment

> **Your task is simple:** no matter the size of the world, Karel should fill it with beepers.

For example, consider Karel's starting **5×5 world**. When complete, it should look like this:

```
◆   ◆   ◆   ◆   ◆
◆   ◆   ◆   ◆   ◆
◆   ◆   ◆   ◆   ◆
◆   ◆   ◆   ◆   ◆
◆   ◆   ◆   ◆   K→   (K = Karel, facing right)
```

> ⚠️ **Karel's final position matters.**
> Karel should end in the **top-right corner, facing right**.
> You can assume Karel always **starts in the bottom-left corner, facing right**.

Your code needs to work on **more than just a 5×5 world**. For example, if you run your solution on a **3×4 world**:

```
Before                  After

+   +   +   +           ◆   ◆   ◆   ◆
+   +   +   +     →      ◆   ◆   ◆   ◆
K→  +   +   +           ◆   ◆   ◆   K→
```

The result should still be a world completely filled with beepers.

---

## 🧱 Rules

| # | Rule |
|---|------|
| 1 | Karel starts in the **bottom-left** corner, facing **right**. |
| 2 | Karel must end in the **top-right** corner, facing **right**. |
| 3 | The solution must work for **any world size**, not just 5×5. |
| 4 | Every world has **walls between rows**, blocking upward movement — **except in the first column**. |

---

## 💡 Hint

> How can you fill the world without running into any of the walls?
>
> If you find this problem challenging... **good, it is!** 🎯
> Watch **Lesson 3: Decomposition** for guidance.

---

<div align="center">
<sub>Karel the Robot · Stanford CS106A</sub>
</div>
