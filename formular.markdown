**Influence Score** $S_{\text{ij}}$ The influence score between
project $\text{i}$ and project $\text{j}$ is calculated as:

$$S_{\text{ij}} = 0.5 \cdot T_{\text{ij}} + 0.3 \cdot G_{\text{ij}} + 0.2 \cdot C_{\text{ij}}$$

-   **Technology (**$T_{\text{ij}}$**)**:

    -   $T_{\text{ij}}$*= 1* if both projects share the same technology,
        otherwise $T_{\text{ij}}$*= 0*.

-   **Geography** $G_{\text{ij}}$:

    -   $G_{\text{ij}}$*= 1* if both projects are in the same country,
        otherwise $G_{\text{ij}}$ *= 0*.

-   **Capacity** $C_{\text{ij}}$:

    -   Calculated as:
        $C_{\text{ij}} = 1 - \frac{\left| C_{i} - C_{j} \right|}{\text{Maximum capacity}}$

The closer the capacities, the higher $C_{\text{ij}}$ (between 0 and 1).

**Effect of a Change (**$\mathrm{\Delta}P_{j}$**):** When a parameter
(e.g., capacity) of project $\text{i~}$ changes
($\mathrm{\Delta}P_{i}$), the impact on project $\text{j~}$ is
calculated as:

$$\Delta Pj = S_{\text{ij}} \cdot \Delta P_{i}$$

**Example 1: Similar Projects** Comparing Project 2 and Project 3:

-   **Project 2:** Technology: \"Others/Various\", Country: \"SWE\",
    Capacity: 220.86 kt H2/y.

-   **Project 3:** Technology: \"Others/Various\", Country: \"SWE\",
    Capacity: 287.12 kt H2/y.

**Calculation:**

$T_{23}$*= 1 = 1*, $G_{23}$*= 1*, and
$C_{23} = 1 - \frac{\left| 220.86 - 287.12 \right|}{287.12} \approx 0.769.$

$$S_{23} = 0.5 \cdot 1 + 0.3 \cdot 1 + 0.2 \cdot 0.769 = 0.9538.$$

**Impact:** If Project 2's capacity increases by
$\Delta\text{Capacity}_{2} = 10$, Project 3's capacity increases by
$\Delta\text{Capacity}_{3} = 0.9538 \cdot 10 = 9.54$.

**Example 2: Diverse Projects** Comparing Project 1 and Project 25:

-   **Project 1:** Technology: \"Unknown\", Country: \"DEU\", Capacity:
    0.25 kt H2/y.

-   **Project 25:** Technology: \"Others/Various\", Country: \"EGY\",
    Capacity: 25396.34 kt H2/y.

**Calculation:**

1.  $T_{\text{ij}} = 0$, $G_{\text{ij}} = 0$, and
    $C_{\text{ij}} = 1 - \frac{\left| 0.25 - 25396.34 \right|}{25396.34} \approx 0.00001$.

2.  $S_{\text{ij}} = 0.5 \cdot 0 + 0.3 \cdot 0 + 0.2 \cdot 0.00001 = 0.000002$.

**Impact:** The influence of changes in Project 1 on Project 25 is
negligible.

**Why the weights?** The weights (*0.5, 0.3, 0.2*) reflect the assumed
importance of each factor:

-   **Technology (0.5):** Largest impact due to shared technology
    dependencies.

-   **Geography (0.3):** Medium impact due to shared markets or
    infrastructure.

-   **Capacity (0.2):** Smaller impact as capacity differences are less
    direct.

**ALL CALCULATIONS ABOVE ALSO GO FOR THE COSTS OF A PROJECT (Use
Investment Cost (MUSD) instead of Capacity (kt H2/y)).**
