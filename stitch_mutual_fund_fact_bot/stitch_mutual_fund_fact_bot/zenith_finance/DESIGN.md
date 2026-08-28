---
name: Zenith Finance
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0edec'
  surface-container-high: '#ebe7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#3e4a3f'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#6e7a6f'
  outline-variant: '#bdcabc'
  surface-tint: '#006d38'
  primary: '#006935'
  on-primary: '#ffffff'
  primary-container: '#008545'
  on-primary-container: '#eeffed'
  inverse-primary: '#71dc92'
  secondary: '#0057bf'
  on-secondary: '#ffffff'
  secondary-container: '#2670e3'
  on-secondary-container: '#fefcff'
  tertiary: '#9d3747'
  on-tertiary: '#ffffff'
  tertiary-container: '#bd4f5e'
  on-tertiary-container: '#fff9f9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#8df9ac'
  primary-fixed-dim: '#71dc92'
  on-primary-fixed: '#00210d'
  on-primary-fixed-variant: '#005228'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#aec6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004396'
  tertiary-fixed: '#ffdadb'
  tertiary-fixed-dim: '#ffb2b8'
  on-tertiary-fixed: '#40000f'
  on-tertiary-fixed-variant: '#832334'
  background: '#FFFFFF'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
  surface-subtle: '#F3F4F6'
  border-light: '#E5E7EB'
  status-warning: '#F59E0B'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
  data-numeric:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system is engineered for a high-trust, data-centric financial assistant. It bridges the gap between sophisticated fintech platforms and conversational AI, prioritizing clarity and immediate comprehension. 

The aesthetic is **Modern Corporate Minimalism**. It utilizes expansive whitespace, a disciplined color application, and a rigorous information hierarchy to distill complex financial data—such as expense ratios and NAV trends—into digestible insights. The tone is objective, professional, and precise, avoiding decorative elements in favor of functional, high-density layouts that feel both lightweight and authoritative.

## Colors
The palette is rooted in financial stability and growth. 
- **Primary Green (#008545):** Used for "Growth" signals, primary actions, and brand identification. It signifies prosperity and trust.
- **Secondary Blue (#0E65D7):** Reserved for links, secondary interactive elements, and educational tooltips.
- **Neutral Core:** Pure white (#FFFFFF) is the primary canvas to ensure maximum legibility. Off-white/Gray (#F3F4F6) is used for container backgrounds to separate the FAQ assistant's responses from the user's queries.
- **Semantic Accents:** A specialized warning color is used for mandatory disclaimers to ensure regulatory visibility without appearing alarming.

## Typography
Inter is the sole typeface, utilized for its exceptional legibility in small sizes and its neutral, systematic feel.
- **Headlines:** Bold weights with negative letter-spacing create a compact, professional appearance for fund names and section headers.
- **Body:** Standardized at 14px for density. Line heights are generous (1.5x) to ensure long FAQ answers remain readable.
- **Data-Numeric:** A specific style for financial figures (NAV, Ratios) that uses medium/semibold weights to stand out within body text.
- **Disclaimers:** Use `label-sm` with a slightly muted text color to satisfy legal requirements while maintaining a clean UI.

## Layout & Spacing
The layout follows a **Fixed Grid** model on desktop (max-width 1200px) and a fluid single-column model on mobile. 

- **The Chat Interface:** Uses a centered column (max-width 800px) to keep financial data within the user's primary field of vision. 
- **Information Density:** Spacing is tight (8px or 16px increments) within data cards (like Fund Details) to allow users to compare expense ratios and exit loads without excessive scrolling.
- **Breakpoints:**
  - Mobile (< 640px): 16px horizontal margins.
  - Tablet (640px - 1024px): 32px horizontal margins, 2-column data grids.
  - Desktop (> 1024px): 12-column grid, 24px gutters.

## Elevation & Depth
This design system avoids heavy shadows, favoring **Tonal Layers** and **Low-contrast Outlines** to define depth.

- **Level 0 (Background):** Pure White (#FFFFFF).
- **Level 1 (Cards/Inputs):** Defined by a 1px solid border (#E5E7EB). No shadow.
- **Level 2 (Active/Hover):** Subtle 1px Primary Green border or a very soft, diffused shadow (0px 4px 12px rgba(0,0,0,0.05)).
- **Separation:** Assistant responses use the Surface-Subtle background (#F3F4F6) to create a clear visual distinction from user prompts without needing elevation.

## Shapes
The shape language is "Soft" (4px - 8px radius) to maintain a modern, approachable feel while retaining the structural integrity expected of a financial institution. 
- **Standard Radius:** 4px (0.25rem) for buttons, inputs, and small chips.
- **Container Radius:** 8px (0.5rem) for large response cards and fund summary modules.
- **Search Bars:** Rounded-xl (12px) to differentiate global navigation/search from data containers.

## Components
- **Buttons:** Primary buttons use a solid Green (#008545) background with white text. Secondary buttons are ghost-style with a 1px Blue (#0E65D7) border.
- **Data Chips:** Small, 4px rounded tags with subtle gray backgrounds used for "Equity", "Debt", or "Tax Saver" categories.
- **Financial Cards:** White background, 1px Gray border. These cards use a 2-column key-value pair layout for data like "Expense Ratio: 0.15%".
- **Disclaimer Block:** A distinct component with a 1px left-accent border in `status-warning` (Amber) and a light cream or off-white background. Text is `label-sm`.
- **Input Fields:** Minimalist design; 1px border that turns Green on focus. Labels are `label-md` in a neutral gray above the field.
- **FAQ Accordions:** Clean lines, no fill. Uses a simple chevron icon. The header remains `headline-sm` for easy scanning.