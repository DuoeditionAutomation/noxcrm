# 🎨 Guia de Customização e UX/UI

Este guia ajuda você a personalizar o Sistema de Orçamento VivaCRM conforme sua marca.

## 🎯 Customização de Cores

### Alterar Cores Principais

Edite `static/css/style.css` e procure por `:root`:

```css
:root {
    --primary-color: #FF6B35;      /* Cor principal (botões, destaques) */
    --primary-dark: #E85A29;       /* Cor escura para hover */
    --secondary-color: #1a1a1a;    /* Cor escura (textos, títulos) */
    --text-color: #333;             /* Cor do texto padrão */
    --text-light: #666;             /* Cor do texto mais clara */
    --background-color: #f7f7f7;   /* Cor de fundo */
    --success-color: #4CAF50;      /* Cor de sucesso */
    --error-color: #f44336;         /* Cor de erro */
}
```

### Exemplo: Mudar para Azul e Preto

```css
:root {
    --primary-color: #1E88E5;       /* Azul vibrante */
    --primary-dark: #1565C0;        /* Azul escuro */
    --secondary-color: #000000;     /* Preto puro */
    /* ... resto das cores ... */
}
```

## 🖼️ Personalizar Logo

### Opção 1: Mudar Logo SVG

1. Coloque seu arquivo SVG em `assets/seu-logo.svg`
2. Edite `templates/index.html`:

```html
<img src="{{ url_for('static', filename='../assets/seu-logo.svg') }}" alt="VivaCRM Logo" class="logo">
```

### Opção 2: Usar Logo PNG

1. Coloque seu PNG em `assets/logo.png`
2. Edite `templates/index.html` e ajuste:

```html
<img src="{{ url_for('static', filename='../assets/logo.png') }}" alt="VivaCRM Logo" class="logo">
```

### Opção 3: Ajustar Tamanho do Logo

No `static/css/style.css`, altere:

```css
.logo-container {
    height: 120px;  /* Aumentar ou diminuir */
}

.logo {
    max-width: 100%;
    max-height: 100%;
}
```

## 🎬 Tipos de Trabalho (Customização)

Edite `templates/index.html` e procure por `<select id="tipo_trabalho">`:

```html
<select id="tipo_trabalho" name="tipo_trabalho" required>
    <option value="">-- Selecione --</option>
    <option value="Instalação de Persianas">Instalação de Persianas</option>
    <option value="Cortinas">Cortinas</option>
    <!-- ADICIONE AQUI -->
    <option value="Seu Novo Tipo">Seu Novo Tipo</option>
</select>
```

### Exemplo: Para Vidraçaria

```html
<select id="tipo_trabalho" name="tipo_trabalho" required>
    <option value="">-- Selecione --</option>
    <option value="Box Vidro">Box Vidro</option>
    <option value="Espelho">Espelho</option>
    <option value="Vidro Temperado">Vidro Temperado</option>
    <option value="Vidro Jateado">Vidro Jateado</option>
    <option value="Manutenção">Manutenção</option>
</select>
```

## 🛠️ Materiais (Customização)

Edite `templates/index.html` e procure por `<div class="checkbox-group">`:

```html
<div class="checkbox-group">
    <label class="checkbox-item">
        <input type="checkbox" name="materiais" value="Seu Material">
        <span>Seu Material</span>
    </label>
    <!-- REPITA PARA CADA MATERIAL -->
</div>
```

### Exemplo: Materiais para Construção

```html
<div class="checkbox-group">
    <label class="checkbox-item">
        <input type="checkbox" name="materiais" value="Argamassa">
        <span>Argamassa</span>
    </label>
    <label class="checkbox-item">
        <input type="checkbox" name="materiais" value="Cimento">
        <span>Cimento</span>
    </label>
    <label class="checkbox-item">
        <input type="checkbox" name="materiais" value="Areia">
        <span>Areia</span>
    </label>
    <label class="checkbox-item">
        <input type="checkbox" name="materiais" value="Tijolos">
        <span>Tijolos</span>
    </label>
</div>
```

## 🎨 Temas Pré-configurados

### Tema 1: Laranja (Padrão)

Já está implementado!

### Tema 2: Azul Profissional

```css
:root {
    --primary-color: #0066cc;
    --primary-dark: #0052a3;
    --secondary-color: #003d82;
    --text-color: #1a1a1a;
    --text-light: #666;
    --background-color: #f0f4f8;
    --success-color: #0066cc;
    --error-color: #cc0000;
}
```

### Tema 3: Verde Sustainability

```css
:root {
    --primary-color: #2ecc71;
    --primary-dark: #27ae60;
    --secondary-color: #1e5631;
    --text-color: #2c3e50;
    --text-light: #7f8c8d;
    --background-color: #ecf0f1;
    --success-color: #2ecc71;
    --error-color: #e74c3c;
}
```

### Tema 4: Roxo Premium

```css
:root {
    --primary-color: #8e44ad;
    --primary-dark: #6c3483;
    --secondary-color: #4a235a;
    --text-color: #2e2e2e;
    --text-light: #757575;
    --background-color: #f5f5f5;
    --success-color: #8e44ad;
    --error-color: #e74c3c;
}
```

## 📱 Ajustar Layout

### Aumentar Largura Máxima do Formulário

Em `static/css/style.css`:

```css
.container {
    max-width: 700px;  /* Padrão */
    /* Mudar para: */
    max-width: 900px;  /* Mais largo */
    /* Ou: */
    max-width: 500px;  /* Mais estreito */
}
```

### Adicionar Fundo Customizado

```css
body {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    /* Mudar para: */
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

## 🔤 Mudar Fontes

### Usar Google Fonts

Edite `templates/index.html` e adicione no `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
```

Depois em `static/css/style.css`:

```css
body {
    font-family: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
```

### Outras Opções de Fontes

- **Inter**: Moderna e limpa
- **Roboto**: Versátil e profissional
- **Playfair Display**: Elegante e sofisticada
- **Space Mono**: Técnica e moderna

## 🎬 Animações

### Desabilitar Animações (Performance)

Em `static/css/style.css`, altere:

```css
:root {
    --transition: none; /* Era: all 0.3s ... */
}
```

### Aumentar Velocidade de Animações

```css
:root {
    --transition: all 0.1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
```

### Adicionar Nova Animação

```css
@keyframes slideFromLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.form-phase {
    animation: slideFromLeft 0.5s ease !important;
}
```

## 📝 Customizar Textos

### Títulos e Labels

Edite `templates/index.html`:

```html
<h1>Sistema de Orçamento</h1>
<!-- Mudar para: -->
<h1>Solicitar Orçamento - VivaCRM</h1>

<h2>Informações do Cliente</h2>
<!-- Mudar para: -->
<h2>Dados Pessoais</h2>
```

### Labels de Button

```html
<button type="button" class="btn btn-primary next-phase">
    Próximo
</button>

<!-- Mudar para: -->
<button type="button" class="btn btn-primary next-phase">
    Continuar →
</button>
```

## 🎯 Ícones Customizados

### Adicionar SVG Customizado

Substitua o SVG inline no HTML. Procure por:

```html
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M5 12h14M12 5l7 7-7 7"/>
</svg>
```

Encontre SVGs em:
- [Feather Icons](https://feathericons.com/)
- [Heroicons](https://heroicons.com/)
- [Tabler Icons](https://tabler-icons.io/)

## 📊 Exemplo Completo: Tema Escuro

```css
:root {
    --primary-color: #00ff88;       /* Verde neon */
    --primary-dark: #00cc6a;
    --secondary-color: #0d1117;     /* Preto muito escuro */
    --text-color: #c9d1d9;          /* Branco claro */
    --text-light: #8b949e;          /* Cinza */
    --border-color: #30363d;        /* Cinza escuro */
    --background-color: #161b22;    /* Preto */
}

body {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
    color: var(--text-color);
}
```

## 🔗 Recursos de Design

- **Material Design**: https://material.io/
- **Dribbble**: https://dribbble.com/
- **Figma Community**: https://figma.com/community
- **Color Palettes**: https://coolors.co/
- **Font Combinação**: https://fontpair.co/

## 💡 Dicas Importantes

1. **Testar em Mobile**: Sempre check em celular
2. **Contraste**: Certifique-se que textos são legíveis
3. **Acessibilidade**: Use cores que funcionem para daltônicos
4. **Marca**: Mantenha consistência com sua identidade visual
5. **Performance**: Não exagere em animações

## 🎨 Paletas de Cores Recomendadas

### Negócios
```
Principal: #2C3E50 (Azul-Escuro)
Secundária: #E74C3C (Vermelho)
Sucesso: #27AE60 (Verde)
```

### Criativo
```
Principal: #9B59B6 (Roxo)
Secundária: #3498DB (Azul)
Destaque: #F39C12 (Ouro)
```

### Tecnologia
```
Principal: #34495E (Cinza Escuro)
Secundária: #1ABC9C (Turquesa)
Sucesso: #2ECC71 (Verde Claro)
```

---

**Divirta-se customizando!** 🎨✨
