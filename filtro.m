function g = filtro(f)
    wc = 2*pi*f
    s = tf("s")
    G = wc^2 / (s^2 + 2*wc*s + wc^2)
    syms z
    T = 1/44100
    g = c2d(G, T)
end