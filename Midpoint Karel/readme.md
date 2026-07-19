<div align="center">

# 🤖 Karel: Midpoint of 1st Street

### *Stanford CS106A — Karel the Robot*

</div>

---

## 📋 Assignment

> As an exercise in solving algorithmic problems, you will program Karel to find the **midpoint of 1st Street**.

Say Karel starts in the **5×5 world**. Karel should end in the **center of 1st row**.

**Before:**

```
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
K→  +   +   +   +
```

**After:**

```
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
+   +   ◆K→ +   +
```

> ⚠️ The final configuration of the world should have **only a single beeper**, placed at the midpoint of the 1st row.
>
> Along the way, Karel **is allowed** to place additional beepers wherever it needs to — but must **pick them all up again** before finishing. Likewise, if Karel paints/colors any corners of the world, they must **all be uncolored** before Karel finishes.

---

## 🧱 Facts you can count on

| # | Fact |
|---|------|
| 1 | Karel starts at the **bottom-left corner** of the world, facing **east**. |
| 2 | The initial state of the world includes **no interior walls or beepers**. |
| 3 | The world **need not be square** — but you may assume it is **at least as tall as it is wide**. |
| 4 | If the **width is odd**, Karel must put the beeper in the **center square**. |
| 5 | If the **width is even**, Karel must drop the beeper on the **left-most of the two center squares**. |

---

## 💡 Notes

> There are many different algorithms you can use to solve this problem — feel free to be creative!
>
> Your program should run successfully in **all possible worlds**, not just the 5×5 example.

---

<div align="center">
<sub>Karel the Robot · Stanford CS106A</sub>
</div>
