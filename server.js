const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, 'templates')));

const EXACT_CODES = [
  'C910', 'C920', 'C930', 'C940', 'C950', 'C960', 'C970', 'C980', 'C990', 'C1000',
  'C911', 'C921', 'C931', 'C941', 'C951', 'C961', 'C971', 'C981', 'C991', 'C1001'
];

let usersDb = EXACT_CODES.map(code => ({
  id: code,
  aluminio: 0.0,
  pet: 0.0,
  papel: 0.0
}));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'templates', 'index.html'));
});

app.get('/api/users', (req, res) => {
  res.json(usersDb);
});

app.put('/api/users/:user_id', (req, res) => {
  const { user_id } = req.params;
  const data = req.body;
  const user = usersDb.find(u => u.id === user_id);

  if (user) {
    if (data.aluminio !== undefined) user.aluminio = parseFloat(data.aluminio);
    if (data.pet !== undefined) user.pet = parseFloat(data.pet);
    if (data.papel !== undefined) user.papel = parseFloat(data.papel);
    return res.json({ status: 'success', user });
  }
  return res.status(404).json({ status: 'error', message: 'Usuário não encontrado' });
});

app.post('/api/reset', (req, res) => {
  usersDb = EXACT_CODES.map(code => ({
    id: code,
    aluminio: 0.0,
    pet: 0.0,
    papel: 0.0
  }));
  res.json({ status: 'success', users: usersDb });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});