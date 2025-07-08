import { useState, Fragment } from 'react';
import { Dialog, Transition } from '@headlessui/react';
import teams from '../data/teams';

const TeamSelector = ({ selectedTeam, setSelectedTeam }) => {
  const [isOpen, setIsOpen] = useState(false);

  const closeModal = () => setIsOpen(false);
  const openModal = () => setIsOpen(true);

  const handleSelect = (team) => {
    setSelectedTeam(team);
    closeModal();
  };

  return (
    <>
      <button
        type="button"
        onClick={openModal}
        className="w-full border rounded-md p-2 flex items-center space-x-2 hover:ring-2 hover:ring-blue-500"
      >
        {selectedTeam ? (
          <>
            <img src={selectedTeam.logo} alt={selectedTeam.name} className="w-6 h-6 object-contain" />
            <span>{selectedTeam.name}</span>
          </>
        ) : (
          <span className="text-gray-500">Select a team</span>
        )}
      </button>

      <Transition appear show={isOpen} as={Fragment}>
        <Dialog as="div" className="relative z-50" onClose={closeModal}>
          {/* Background overlay */}
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300" enterFrom="opacity-0" enterTo="opacity-100"
            leave="ease-in duration-200" leaveFrom="opacity-100" leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-40" />
          </Transition.Child>

          {/* Modal content */}
          <div className="fixed inset-0 flex items-center justify-center p-4">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300" enterFrom="opacity-0 scale-95" enterTo="opacity-100 scale-100"
              leave="ease-in duration-200" leaveFrom="opacity-100 scale-100" leaveTo="opacity-0 scale-95"
            >
              <Dialog.Panel className="bg-white rounded-lg p-6 max-w-md max-h-[70vh] overflow-auto">
                <Dialog.Title className="text-xl font-semibold mb-4 text-center">
                  Select a Team
                </Dialog.Title>

                <div className="grid grid-cols-4 gap-4">
                  {teams.map((team) => (
                    <button
                      key={team.name}
                      onClick={() => handleSelect(team)}
                      className={`flex flex-col items-center space-y-1 p-2 rounded hover:bg-blue-100 ${
                        selectedTeam?.name === team.name ? 'ring-2 ring-blue-500' : ''
                      }`}
                    >
                      <img src={team.logo} alt={team.name} className="w-16 h-16 object-contain" />
                      <span className="text-sm">{team.name}</span>
                    </button>
                  ))}
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </Dialog>
      </Transition>
    </>
  );
};

export default TeamSelector;